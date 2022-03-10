// Decompiled with JetBrains decompiler
// Type: B450_Testbench.B450_Labview
// Assembly: B450_Labview_V3, Version=1.0.0.1, Culture=neutral, PublicKeyToken=null
// MVID: 83C7D531-E990-492D-9D70-D78678AED62E
// Assembly location: \\Mac\Home\Documents\RTD31DApp\data\B450_Labview_V2.dll

using System;
using System.Collections.Concurrent;

namespace B450_Testbench
{
  public class B450_Labview
  {
    private bool good;
    private B450Comms comms;
    private ConcurrentQueue<ECG_Values> value_ECG;
    private ConcurrentQueue<PPG_Values> value_PPG;
        private ConcurrentQueue<NIBP_values> value_NIBP;
    private ConcurrentQueue<short> waveform_ECG;
    private ConcurrentQueue<short> waveform_PPG;
    private ConcurrentQueue<short> waveform_RES;
    private ConcurrentQueue<string> errors;
    private volatile bool ecg_leads_off = true;
    private volatile bool ppg_leads_off = true;
    private volatile bool res_leads_off = true;

    public B450_Labview(string portname)
    {
      this.value_ECG = new ConcurrentQueue<ECG_Values>();
      this.value_PPG = new ConcurrentQueue<PPG_Values>();
      this.value_NIBP = new ConcurrentQueue<NIBP_values>();
      this.waveform_ECG = new ConcurrentQueue<short>();
      this.waveform_PPG = new ConcurrentQueue<short>();
      this.waveform_RES = new ConcurrentQueue<short>();
      this.errors = new ConcurrentQueue<string>();
      this.comms = new B450Comms(portname);
      this.comms.OnRawDataReceived += new B450Comms.RawDataReceivedEventHandler(this.comms_OnRawDataReceived);
      this.good = this.comms.Open();
      if (!this.good)
      {
        this.errors.Enqueue("Failed to open serial communications.");
        Console.WriteLine("Failed to open serial communications.");
      }
      else
      {
        if (this.comms.WriteAppData(B450Comms.GenerateDatabaseRequest(DRI_PHYSIO_TYPE.Displayed, (short) 5, DRI_LEVEL.Level2009)))
        {
          if (this.comms.WriteAppData(B450Comms.GenerateWaveformRequest(WAVEFORM_MODE.Start, WAVEFORM_CHANNEL.ECG1, WAVEFORM_CHANNEL.RESP, WAVEFORM_CHANNEL.PPG1)))
            return;
        }
        this.good = false;
        this.errors.Enqueue("Failed to talk to B450.");
        Console.WriteLine("Failed to talk to B450.");
      }
    }

    public void Dispose()
    {
      try
      {
        this.comms.WriteAppData(B450Comms.GenerateDatabaseRequest(DRI_PHYSIO_TYPE.Displayed, (short) 0, DRI_LEVEL.Level2009));
        this.comms.WriteAppData(B450Comms.GenerateWaveformRequest(WAVEFORM_MODE.Stop, WAVEFORM_CHANNEL.ECG1, WAVEFORM_CHANNEL.RESP, WAVEFORM_CHANNEL.PPG1));
        this.comms.Close();
        this.comms.Dispose();
      }
      catch (Exception ex)
      {
        this.errors.Enqueue(ex.Message);
        Console.WriteLine(ex.Message);
      }
    }

    private unsafe void comms_OnRawDataReceived(B450Comms sender, byte[] data)
    {
      B450Comms.Record recordFromBytes = B450Comms.GetRecordFromBytes(data, out DateTime _);
      if (recordFromBytes.Header.MainType == (short) 0)
      {
        B450Comms.PhysiologicalDataBase physiologicalDatabase = B450Comms.ParsePhysiologicalDatabase(recordFromBytes);
        this.value_ECG.Enqueue(new ECG_Values()
        {
          HR_Primary = physiologicalDatabase.Basic.ecg.hr,
          HR_Source = (HR_Source) (physiologicalDatabase.Basic.ecg.hdr.status_bits >> 3 & 15U),
          HeartRate = physiologicalDatabase.Basic.ecg_extra.hr_ecg,
          HeartRate_Max = physiologicalDatabase.Basic.ecg_extra.hr_max,
          HeartRate_Min = physiologicalDatabase.Basic.ecg_extra.hr_min,
          Asystole = ((int) physiologicalDatabase.Basic.ecg.hdr.status_bits & 4) != 0,
          Noise = ((int) physiologicalDatabase.Basic.ecg.hdr.status_bits & 128) != 0,
          Artifact = ((int) physiologicalDatabase.Basic.ecg.hdr.status_bits & 256) != 0,
          Learning = ((int) physiologicalDatabase.Basic.ecg.hdr.status_bits & 512) != 0,
          Channel1Off = ((int) physiologicalDatabase.Basic.ecg.hdr.status_bits & 2048) != 0,
          Channel2Off = ((int) physiologicalDatabase.Basic.ecg.hdr.status_bits & 4096) != 0,
          Channel3Off = ((int) physiologicalDatabase.Basic.ecg.hdr.status_bits & 8192) != 0,
          ECGLeadsOff = this.ecg_leads_off,
          RespLeadsOff = this.res_leads_off
        });
        this.value_PPG.Enqueue(new PPG_Values()
        {
          PulseRate = physiologicalDatabase.Basic.SpO2.pr,
          Modulation = physiologicalDatabase.Basic.SpO2.ir_amp,
          SPO2_Percent = physiologicalDatabase.Basic.SpO2.SpO2
        });
        this.value_NIBP.Enqueue(new NIBP_values()
        {
          SBP = physiologicalDatabase.Basic.nibp.sys,
          DBP = physiologicalDatabase.Basic.nibp.dia,
          MBP = physiologicalDatabase.Basic.nibp.mean,
          HR = physiologicalDatabase.Basic.nibp.hr
        });

      }
      else if (recordFromBytes.Header.MainType == (short) 1)
      {
        B450Comms.WaveformDataBase waveforms = B450Comms.ParseWaveforms(recordFromBytes);
        for (int index1 = 0; index1 < waveforms.NumberChannels; ++index1)
        {
          B450Comms.WaveformChannel waveformChannel = new B450Comms.WaveformChannel();
          switch (index1)
          {
            case 0:
              waveformChannel = waveforms.Channel0;
              break;
            case 1:
              waveformChannel = waveforms.Channel1;
              break;
            case 2:
              waveformChannel = waveforms.Channel2;
              break;
            case 3:
              waveformChannel = waveforms.Channel3;
              break;
          }
          switch (waveformChannel.Type)
          {
            case WAVEFORM_CHANNEL.ECG1:
              this.ecg_leads_off = ((int) waveformChannel.Header.status & 8) != 0;
              for (int index2 = 0; index2 < (int) waveformChannel.Header.act_len; ++index2)
                this.waveform_ECG.Enqueue(waveformChannel.Data[index2]);
              break;
            case WAVEFORM_CHANNEL.PPG1:
              this.ppg_leads_off = ((int) waveformChannel.Header.status & 8) != 0;
              for (int index3 = 0; index3 < (int) waveformChannel.Header.act_len; ++index3)
                this.waveform_PPG.Enqueue(waveformChannel.Data[index3]);
              break;
            case WAVEFORM_CHANNEL.RESP:
              this.res_leads_off = ((int) waveformChannel.Header.status & 8) != 0;
              for (int index4 = 0; index4 < (int) waveformChannel.Header.act_len; ++index4)
                this.waveform_RES.Enqueue(waveformChannel.Data[index4]);
              break;
          }
        }
      }
      else
      {
        this.errors.Enqueue("Unknown data from B450!");
        Console.WriteLine("Unknown data from B450!");
      }
    }

    public bool Good => this.good;

    public bool Has_ECG_Values => this.value_ECG != null && !this.value_ECG.IsEmpty;

    public bool Has_PPG_Values => this.value_PPG != null && !this.value_PPG.IsEmpty;

    public bool Has_NIBP_Values => this.value_NIBP!= null && !this.value_NIBP.IsEmpty;

    public bool Has_ECG_Waveform => this.waveform_ECG != null && !this.waveform_ECG.IsEmpty;

    public bool Has_PPG_Waveform => this.waveform_PPG != null && !this.waveform_PPG.IsEmpty;

    public bool Has_RES_Waveform => this.waveform_RES != null && !this.waveform_RES.IsEmpty;

    public bool Has_Errors => this.errors != null && !this.errors.IsEmpty;

    public ECG_Values Next_ECG_Values
    {
      get
      {
        ECG_Values result = new ECG_Values();
        if (this.value_ECG != null)
          this.value_ECG.TryDequeue(out result);
        return result;
      }
    }

    public PPG_Values Next_PPG_Values
    {
      get
      {
        PPG_Values result = new PPG_Values();
        if (this.value_PPG != null)
          this.value_PPG.TryDequeue(out result);
        return result;
      }
    }

    public NIBP_values Next_NIBP_Values
    {
        get
        {
            NIBP_values result = new NIBP_values();
            if (this.value_NIBP != null)
                this.value_NIBP.TryDequeue(out result);
            return result;
        }
    }

        public int Next_ECG_Waveform
    {
      get
      {
        short result = short.MinValue;
        if (this.waveform_ECG != null)
          this.waveform_ECG.TryDequeue(out result);
        return (int) result;
      }
    }

    public int Next_PPG_Waveform
    {
      get
      {
        short result = short.MinValue;
        if (this.waveform_PPG != null)
          this.waveform_PPG.TryDequeue(out result);
        return (int) result;
      }
    }

    public int Next_RES_Waveform
    {
      get
      {
        short result = short.MinValue;
        if (this.waveform_RES != null)
          this.waveform_RES.TryDequeue(out result);
        return (int) result;
      }
    }

    public string Next_Error
    {
      get
      {
        string result = "<no error>";
        if (this.errors != null)
          this.errors.TryDequeue(out result);
        return result;
      }
    }

    public int Num_ECG_Values => this.value_ECG == null ? -1 : this.value_ECG.Count;

    public int Num_PPG_Values => this.value_PPG == null ? -1 : this.value_PPG.Count;

    public int Num_NIBP_Values => this.value_NIBP == null ? -1 : this.value_NIBP.Count;

    public int Num_ECG_Waveform => this.waveform_ECG == null ? -1 : this.waveform_ECG.Count;

    public int Num_PPG_Waveform => this.waveform_PPG == null ? -1 : this.waveform_PPG.Count;

    public int Num_RES_Waveform => this.waveform_RES == null ? -1 : this.waveform_RES.Count;

    public int Num_Errors => this.errors == null ? -1 : this.errors.Count;
  }
}
