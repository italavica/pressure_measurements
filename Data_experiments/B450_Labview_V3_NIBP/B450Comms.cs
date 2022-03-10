// Decompiled with JetBrains decompiler
// Type: B450_Testbench.B450Comms
// Assembly: B450_Labview_V2, Version=1.0.0.1, Culture=neutral, PublicKeyToken=null
// MVID: 83C7D531-E990-492D-9D70-D78678AED62E
// Assembly location: \\Mac\Home\Documents\RTD31DApp\data\B450_Labview_V2.dll

using System;
using System.Collections.Generic;
using System.IO.Ports;
using System.Linq;
using System.Runtime.InteropServices;
using System.Text;
using System.Threading;

namespace B450_Testbench
{
  public class B450Comms
  {
    private const byte FRAME_FLAG = 126;
    private const byte FRAME_CONT = 125;
    private const byte FRAME_MASK = 32;
    public const int DRI_MAX_SUBRECS = 8;
    public const int DRI_MAX_PHDBRECS = 5;
    public const short DRI_MT_PHDB = 0;
    public const short DRI_MT_WAVE = 1;
    public const short DRI_MT_ALARM = 4;
    public const uint DRI_PHDBCL_REQ_BASIC_MASK = 0;
    public const uint DRI_PHDBCL_DENY_BASIC_MASK = 1;
    public const uint DRI_PHDBCL_REQ_EXT1_MASK = 2;
    public const uint DRI_PHDBCL_REQ_EXT2_MASK = 4;
    public const uint DRI_PHDBCL_REQ_EXT3_MASK = 8;
    public const int DATA_INVALID_LIMIT = -32001;
    public const int DATA_INVALID = -32767;
    public const int DATA_NOT_UPDATED = -32766;
    public const int DATA_DISCONT = -32765;
    public const int DATA_UNDER_RANGE = -32764;
    public const int DATA_OVER_RANGE = -32763;
    public const int DATA_NOT_CALIBRATED = -32762;
    private SerialPort port;
    private Thread receiveThread;
    private volatile bool receiveRunning;

    public static unsafe byte[] GenerateDatabaseRequest(
      DRI_PHYSIO_TYPE transmission_type,
      short interval,
      DRI_LEVEL dri_level)
    {
      if (interval > (short) 0 && interval < (short) 5)
        interval = (short) 5;
      B450Comms.Database_Record_Request databaseRecordRequest = new B450Comms.Database_Record_Request();
      databaseRecordRequest.Header.Length = (short) 49;
      databaseRecordRequest.Header.DRI_Level = (byte) dri_level;
      databaseRecordRequest.Header.Time = 0U;
      databaseRecordRequest.Header.MainType = (short) 0;
      databaseRecordRequest.Header.SubRecord1.Offset = (short) 0;
      databaseRecordRequest.Header.SubRecord1.Type = (byte) 0;
      databaseRecordRequest.Header.SubRecord2.Offset = (short) 0;
      databaseRecordRequest.Header.SubRecord2.Type = byte.MaxValue;
      databaseRecordRequest.PhysiologicalDataBaseRecord.RecordType = (byte) transmission_type;
      databaseRecordRequest.PhysiologicalDataBaseRecord.TransmissionInterval = interval;
      databaseRecordRequest.PhysiologicalDataBaseRecord.ClassTypeMask = 0U;
      if (databaseRecordRequest.PhysiologicalDataBaseRecord.TransmissionInterval != (short) 0)
        databaseRecordRequest.PhysiologicalDataBaseRecord.ClassTypeMask = 14U;
      byte[] destination = new byte[Marshal.SizeOf(typeof (B450Comms.Database_Record_Request))];
      Marshal.Copy((IntPtr) (void*) &databaseRecordRequest, destination, 0, destination.Length);
      return destination;
    }

    public static unsafe byte[] GenerateWaveformRequest(
      WAVEFORM_MODE mode,
      params WAVEFORM_CHANNEL[] types)
    {
      B450Comms.Waveform_Record_Request waveformRecordRequest = new B450Comms.Waveform_Record_Request();
      waveformRecordRequest.Header.Length = (short) 72;
      waveformRecordRequest.Header.Time = 0U;
      waveformRecordRequest.Header.MainType = (short) 1;
      waveformRecordRequest.Header.SubRecord1.Offset = (short) 0;
      waveformRecordRequest.Header.SubRecord1.Type = (byte) 0;
      waveformRecordRequest.Header.SubRecord2.Offset = (short) 0;
      waveformRecordRequest.Header.SubRecord2.Type = byte.MaxValue;
      waveformRecordRequest.WaveformRequest.RequestType = (short) mode;
      int index = 0;
      if (mode == WAVEFORM_MODE.Start)
      {
        foreach (WAVEFORM_CHANNEL type in types)
          waveformRecordRequest.WaveformRequest.Type[index++] = (byte) type;
      }
      waveformRecordRequest.WaveformRequest.Type[index] = byte.MaxValue;
      byte[] destination = new byte[Marshal.SizeOf(typeof (B450Comms.Waveform_Record_Request))];
      Marshal.Copy((IntPtr) (void*) &waveformRecordRequest, destination, 0, destination.Length);
      return destination;
    }

    public static unsafe B450Comms.Record GetRecordFromBytes(byte[] data, out DateTime dt)
    {
      B450Comms.Record record;
      Marshal.Copy(data, 0, (IntPtr) (void*) &record, Math.Min(data.Length, 1490));
      dt = new DateTime(1970, 1, 1, 0, 0, 0, 0).AddSeconds((double) record.Header.Time);
      return record;
    }

    public static unsafe B450Comms.PhysiologicalDataBase ParsePhysiologicalDatabase(
      B450Comms.Record record)
    {
      B450Comms.SubRecordDescriptor[] recordDescriptorArray = new B450Comms.SubRecordDescriptor[8]
      {
        record.Header.SubRecord1,
        record.Header.SubRecord2,
        record.Header.SubRecord3,
        record.Header.SubRecord4,
        record.Header.SubRecord5,
        record.Header.SubRecord6,
        record.Header.SubRecord7,
        record.Header.SubRecord8
      };
      B450Comms.PhysiologicalDataBase physiologicalDataBase = new B450Comms.PhysiologicalDataBase();
      for (int index1 = 0; index1 < 8 && recordDescriptorArray[index1].Type != byte.MaxValue; ++index1)
      {
        if (recordDescriptorArray[index1].Type == (byte) 1)
        {
          byte[] source = new byte[270];
          for (int index2 = 0; index2 < 270; ++index2)
            source[index2] = record.Payload[4 + index2 + (int) recordDescriptorArray[index1].Offset];
          GCHandle gcHandle = GCHandle.Alloc((object) source, GCHandleType.Pinned);
          switch (index1)
          {
            case 0:
              Marshal.Copy(source, 0, (IntPtr) (void*) &physiologicalDataBase.Basic, source.Length);
              break;
            case 1:
              Marshal.Copy(source, 0, (IntPtr) (void*) &physiologicalDataBase.Ext1, source.Length);
              break;
            case 2:
              Marshal.Copy(source, 0, (IntPtr) (void*) &physiologicalDataBase.Ext2, source.Length);
              break;
            case 3:
              Marshal.Copy(source, 0, (IntPtr) (void*) &physiologicalDataBase.Ext3, source.Length);
              break;
          }
          gcHandle.Free();
        }
      }
      return physiologicalDataBase;
    }

    public static unsafe B450Comms.WaveformDataBase ParseWaveforms(B450Comms.Record record)
    {
      B450Comms.SubRecordDescriptor[] recordDescriptorArray = new B450Comms.SubRecordDescriptor[8]
      {
        record.Header.SubRecord1,
        record.Header.SubRecord2,
        record.Header.SubRecord3,
        record.Header.SubRecord4,
        record.Header.SubRecord5,
        record.Header.SubRecord6,
        record.Header.SubRecord7,
        record.Header.SubRecord8
      };
      B450Comms.WaveformDataBase waveformDataBase = new B450Comms.WaveformDataBase();
      waveformDataBase.NumberChannels = 0;
      for (int index1 = 0; index1 < 8 && recordDescriptorArray[index1].Type != byte.MaxValue; ++index1)
      {
        byte[] source1 = new byte[6];
        for (int index2 = 0; index2 < 6; ++index2)
          source1[index2] = record.Payload[index2 + (int) recordDescriptorArray[index1].Offset];
        B450Comms.WaveformHeader waveformHeader;
        Marshal.Copy(source1, 0, (IntPtr) (void*) &waveformHeader, source1.Length);
        byte[] source2 = new byte[(int) waveformHeader.act_len * 2];
        for (int index3 = 0; index3 < (int) waveformHeader.act_len * 2; ++index3)
          source2[index3] = record.Payload[index3 + (int) recordDescriptorArray[index1].Offset + 6];
        switch (index1)
        {
          case 0:
            ++waveformDataBase.NumberChannels;
            waveformDataBase.Channel0.Type = (WAVEFORM_CHANNEL) recordDescriptorArray[index1].Type;
            waveformDataBase.Channel0.Header = waveformHeader;
            Marshal.Copy(source2, 0, (IntPtr) (void*) waveformDataBase.Channel0.Data, source2.Length);
            break;
          case 1:
            ++waveformDataBase.NumberChannels;
            waveformDataBase.Channel1.Type = (WAVEFORM_CHANNEL) recordDescriptorArray[index1].Type;
            waveformDataBase.Channel1.Header = waveformHeader;
            Marshal.Copy(source2, 0, (IntPtr) (void*) waveformDataBase.Channel1.Data, source2.Length);
            break;
          case 2:
            ++waveformDataBase.NumberChannels;
            waveformDataBase.Channel2.Type = (WAVEFORM_CHANNEL) recordDescriptorArray[index1].Type;
            waveformDataBase.Channel2.Header = waveformHeader;
            Marshal.Copy(source2, 0, (IntPtr) (void*) waveformDataBase.Channel2.Data, source2.Length);
            break;
          case 3:
            ++waveformDataBase.NumberChannels;
            waveformDataBase.Channel3.Type = (WAVEFORM_CHANNEL) recordDescriptorArray[index1].Type;
            waveformDataBase.Channel3.Header = waveformHeader;
            Marshal.Copy(source2, 0, (IntPtr) (void*) waveformDataBase.Channel3.Data, source2.Length);
            break;
        }
      }
      return waveformDataBase;
    }

    public event B450Comms.RawDataReceivedEventHandler OnRawDataReceived;

    public event B450Comms.RawDataTransmittedEventHandler OnRawDataTransmitted;

    private void TriggerRawDataReceived(byte[] data)
    {
      B450Comms.RawDataReceivedEventHandler onRawDataReceived = this.OnRawDataReceived;
      if (onRawDataReceived == null)
        return;
      onRawDataReceived(this, data);
    }

    private void TriggerRawDataTransmitted(byte[] data)
    {
      B450Comms.RawDataTransmittedEventHandler rawDataTransmitted = this.OnRawDataTransmitted;
      if (rawDataTransmitted == null)
        return;
      rawDataTransmitted(this, data);
    }

    public B450Comms(string portname)
    {
      this.port = new SerialPort();
      this.port.PortName = portname;
      this.port.BaudRate = 19200;
      this.port.DataBits = 8;
      this.port.Parity = Parity.Even;
      this.port.StopBits = StopBits.One;
      this.port.Handshake = Handshake.RequestToSend;
      this.port.Encoding = Encoding.GetEncoding(1252);
      this.port.DiscardNull = false;
      this.port.ReadBufferSize = 4096;
      this.port.WriteBufferSize = 4096;
      this.port.ReadTimeout = 500;
      this.port.WriteTimeout = 500;
    }

    public void Dispose() => this.Close();

    public bool Open()
    {
      try
      {
        this.port.Open();
        Thread.Sleep(100);
        this.port.DiscardOutBuffer();
        this.port.DiscardInBuffer();
        this.receiveRunning = true;
        this.receiveThread = new Thread(new ThreadStart(this.ReceiveThreadMain));
        this.receiveThread.Start();
        return true;
      }
      catch
      {
        return false;
      }
    }

    public void Close()
    {
      try
      {
        this.receiveRunning = false;
        this.port.Close();
      }
      catch
      {
      }
    }

    public bool WriteAppData(byte[] data)
    {
      byte[] numArray1 = new byte[data.Length + 1];
      Array.Copy((Array) data, (Array) numArray1, data.Length);
      for (int index = 0; index < data.Length; ++index)
        numArray1[numArray1.Length - 1] = (byte) ((uint) numArray1[numArray1.Length - 1] + (uint) data[index]);
      byte[] data1 = new byte[2 + numArray1.Length + ((IEnumerable<byte>) numArray1).Count<byte>((Func<byte, bool>) (b => b == (byte) 126 || b == (byte) 125))];
      int num1 = 0;
      byte[] numArray2 = data1;
      int index1 = num1;
      int num2 = index1 + 1;
      numArray2[index1] = (byte) 126;
      foreach (byte num3 in numArray1)
      {
        switch (num3)
        {
          case 125:
          case 126:
            byte[] numArray3 = data1;
            int index2 = num2;
            int num4 = index2 + 1;
            numArray3[index2] = (byte) 125;
            byte[] numArray4 = data1;
            int index3 = num4;
            num2 = index3 + 1;
            int num5 = (int) (byte) ((uint) num3 & 4294967263U);
            numArray4[index3] = (byte) num5;
            break;
          default:
            data1[num2++] = num3;
            break;
        }
      }
      byte[] numArray5 = data1;
      int index4 = num2;
      int num6 = index4 + 1;
      numArray5[index4] = (byte) 126;
      try
      {
        this.TriggerRawDataTransmitted(data);
        return this.WriteCTS(data1, 0, data1.Length);
      }
      catch (Exception ex)
      {
        Console.WriteLine("Write FAILED! ({0})", (object) ex.Message);
        return false;
      }
    }

    private bool WaitForCTS(int timeout = 500)
    {
      for (int index = 0; index < timeout; index += 10)
      {
        if (this.port.CtsHolding)
          return true;
        Thread.Sleep(10);
      }
      return false;
    }

    private bool WriteCTS(byte[] data, int start, int length)
    {
      if (!this.WaitForCTS(1000))
        return false;
      for (int offset = start; offset < start + length; ++offset)
      {
        if (!this.WaitForCTS(1000))
          return false;
        this.port.Write(data, offset, 1);
      }
      return true;
    }

    private void ReceiveThreadMain()
    {
      bool flag1 = false;
      bool flag2 = false;
      List<byte> byteList = new List<byte>(100);
      while (this.receiveRunning)
      {
        try
        {
          byte num1 = (byte) this.port.ReadByte();
          if (num1 == (byte) 126)
          {
            if (flag1)
            {
              if (flag2)
              {
                Console.WriteLine("Spare control.");
              }
              else
              {
                byte[] array = byteList.ToArray();
                byte num2 = 0;
                for (int index = 0; index < array.Length - 1; ++index)
                  num2 += array[index];
                if ((int) num2 == (int) array[array.Length - 1])
                  this.TriggerRawDataReceived(byteList.GetRange(0, byteList.Count - 1).ToArray());
                else
                  Console.WriteLine("Checksum error! {0} / {1}", (object) num2, (object) array[array.Length - 1]);
                flag1 = false;
              }
            }
            else
            {
              byteList.Clear();
              flag1 = true;
              flag2 = false;
            }
          }
          else if (flag1)
          {
            if (flag2)
            {
              byteList.Add((byte) ((uint) num1 | 32U));
              flag2 = false;
            }
            else if (num1 == (byte) 125)
              flag2 = true;
            else
              byteList.Add(num1);
          }
        }
        catch (TimeoutException ex)
        {
        }
        catch (Exception ex)
        {
          Thread.Sleep(100);
        }
      }
    }

    [Serializable]
    [StructLayout(LayoutKind.Sequential, Size = 1490, Pack = 1)]
    public struct Record
    {
      public B450Comms.Header Header;
      public unsafe fixed byte Payload[1450];
    }

    [Serializable]
    [StructLayout(LayoutKind.Sequential, Size = 40, Pack = 1)]
    public struct Header
    {
      public short Length;
      public byte r_nbr;
      public byte DRI_Level;
      public ushort plug_id;
      public uint Time;
      private byte reserved1;
      private byte reserved2;
      private ushort reserved3;
      public short MainType;
      public B450Comms.SubRecordDescriptor SubRecord1;
      public B450Comms.SubRecordDescriptor SubRecord2;
      public B450Comms.SubRecordDescriptor SubRecord3;
      public B450Comms.SubRecordDescriptor SubRecord4;
      public B450Comms.SubRecordDescriptor SubRecord5;
      public B450Comms.SubRecordDescriptor SubRecord6;
      public B450Comms.SubRecordDescriptor SubRecord7;
      public B450Comms.SubRecordDescriptor SubRecord8;
    }

    [Serializable]
    [StructLayout(LayoutKind.Sequential, Size = 3, Pack = 1)]
    public struct SubRecordDescriptor
    {
      public short Offset;
      public byte Type;
    }

    [Serializable]
    [StructLayout(LayoutKind.Sequential, Size = 49, Pack = 1)]
    public struct Database_Record_Request
    {
      public B450Comms.Header Header;
      public B450Comms.PhysiologicalDataBase_Request PhysiologicalDataBaseRecord;
    }

    [Serializable]
    [StructLayout(LayoutKind.Sequential, Size = 9, Pack = 1)]
    public struct PhysiologicalDataBase_Request
    {
      public byte RecordType;
      public short TransmissionInterval;
      public uint ClassTypeMask;
      private short reserved;
    }

    [Serializable]
    [StructLayout(LayoutKind.Sequential, Size = 72, Pack = 1)]
    public struct Waveform_Record_Request
    {
      public B450Comms.Header Header;
      public B450Comms.Waveform_Request WaveformRequest;
    }

    [Serializable]
    [StructLayout(LayoutKind.Sequential, Size = 32, Pack = 1)]
    public struct Waveform_Request
    {
      public short RequestType;
      private short res;
      public unsafe fixed byte Type[8];
      private unsafe fixed short reserved[10];
    }

    [StructLayout(LayoutKind.Sequential, Size = 6, Pack = 1)]
    public struct WaveformHeader
    {
      public short act_len;
      public ushort status;
      private short reserved;
    }

    [StructLayout(LayoutKind.Sequential, Pack = 1)]
    public struct WaveformDataBase
    {
      public int NumberChannels;
      public B450Comms.WaveformChannel Channel0;
      public B450Comms.WaveformChannel Channel1;
      public B450Comms.WaveformChannel Channel2;
      public B450Comms.WaveformChannel Channel3;
    }

    [StructLayout(LayoutKind.Sequential, Size = 606, Pack = 1)]
    public struct WaveformChannel
    {
      public B450Comms.WaveformHeader Header;
      public WAVEFORM_CHANNEL Type;
      public unsafe fixed short Data[300];
    }

    [StructLayout(LayoutKind.Sequential, Size = 1088, Pack = 1)]
    public struct PhysiologicalDataBase
    {
      public uint time;
      public B450Comms.PhysiologicalDataBase_Basic Basic;
      public B450Comms.PhysiologicalDataBase_Ext1 Ext1;
      public B450Comms.PhysiologicalDataBase_Ext2 Ext2;
      public B450Comms.PhysiologicalDataBase_Ext3 Ext3;
      public byte Marker;
      private byte reserved;
      public ushort cl_drilvl_subt;
    }

    [StructLayout(LayoutKind.Sequential, Size = 6, Pack = 1)]
    public struct Group_Header
    {
      public uint status_bits;
      public ushort label_info;
    }

    [StructLayout(LayoutKind.Sequential, Size = 270, Pack = 1)]
    public struct PhysiologicalDataBase_Basic
    {
      public B450Comms.ecg_group_type ecg;
      public B450Comms.p_group_type p1;
      public B450Comms.p_group_type p2;
      public B450Comms.p_group_type p3;
      public B450Comms.p_group_type p4;
      public B450Comms.nibp_group_type nibp;
      public B450Comms.t_group_type t1;
      public B450Comms.t_group_type t2;
      public B450Comms.t_group_type t3;
      public B450Comms.t_group_type t4;
      public B450Comms.SpO2_group_type SpO2;
      public B450Comms.co2_group_type co2;
      public B450Comms.o2_group_type o2;
      public B450Comms.n2o_group_type n2o;
      public B450Comms.aa_group_type aa;
      public B450Comms.flow_vol_group_type flow_vol;
      public B450Comms.co_wedge_group_type co_wedge;
      public B450Comms.nmt_group nmt;
      public B450Comms.ecg_extra_group ecg_extra;
      public B450Comms.svo2_group svo2;
      public B450Comms.p_group_type p5;
      public B450Comms.p_group_type p6;
      private unsafe fixed byte reserved[2];
    }

    [StructLayout(LayoutKind.Sequential, Size = 16, Pack = 1)]
    public struct ecg_group_type
    {
      public B450Comms.Group_Header hdr;
      public short hr;
      public short st1;
      public short st2;
      public short st3;
      public short imp_rr;
    }

    [StructLayout(LayoutKind.Sequential, Size = 14, Pack = 1)]
    public struct p_group_type
    {
      public B450Comms.Group_Header hdr;
      public short sys;
      public short dia;
      public short mean;
      public short hr;
    }

    [StructLayout(LayoutKind.Sequential, Size = 14, Pack = 1)]
    public struct nibp_group_type
    {
      public B450Comms.Group_Header hdr;
      public short sys;
      public short dia;
      public short mean;
      public short hr;
    }

    [StructLayout(LayoutKind.Sequential, Size = 8, Pack = 1)]
    public struct t_group_type
    {
      public B450Comms.Group_Header hdr;
      public short temp;
    }

    [StructLayout(LayoutKind.Sequential, Size = 14, Pack = 1)]
    public struct SpO2_group_type
    {
      public B450Comms.Group_Header hdr;
      public short SpO2;
      public short pr;
      public short ir_amp;
      public short svo2;
    }

    [StructLayout(LayoutKind.Sequential, Size = 14, Pack = 1)]
    public struct co2_group_type
    {
      public B450Comms.Group_Header hdr;
      public short et;
      public short fi;
      public short rr;
      public short amb_press;
    }

    [StructLayout(LayoutKind.Sequential, Size = 10, Pack = 1)]
    public struct o2_group_type
    {
      public B450Comms.Group_Header hdr;
      public short et;
      public short fi;
    }

    [StructLayout(LayoutKind.Sequential, Size = 10, Pack = 1)]
    public struct n2o_group_type
    {
      public B450Comms.Group_Header hdr;
      public short et;
      public short fi;
    }

    [StructLayout(LayoutKind.Sequential, Size = 12, Pack = 1)]
    public struct aa_group_type
    {
      public B450Comms.Group_Header hdr;
      public short et;
      public short fi;
      public short mac_sum;
    }

    [StructLayout(LayoutKind.Sequential, Size = 22, Pack = 1)]
    public struct flow_vol_group_type
    {
      public B450Comms.Group_Header hdr;
      public short rr;
      public short ppeak;
      public short peep;
      public short pplat;
      public short tv_insp;
      public short tv_exp;
      public short compliance;
      public short mv_exp;
    }

    [StructLayout(LayoutKind.Sequential, Size = 14, Pack = 1)]
    public struct co_wedge_group_type
    {
      public B450Comms.Group_Header hdr;
      public short co;
      public short blood_temp;
      public short rightef;
      public short pcwp;
    }

    [StructLayout(LayoutKind.Sequential, Size = 12, Pack = 1)]
    public struct nmt_group
    {
      public B450Comms.Group_Header hdr;
      public short t1;
      public short tratio;
      public short ptc;
    }

    [StructLayout(LayoutKind.Sequential, Size = 6, Pack = 1)]
    public struct ecg_extra_group
    {
      public short hr_ecg;
      public short hr_max;
      public short hr_min;
    }

    [StructLayout(LayoutKind.Sequential, Size = 8, Pack = 1)]
    public struct svo2_group
    {
      public B450Comms.Group_Header hdr;
      public short svo2;
    }

    [StructLayout(LayoutKind.Sequential, Size = 270, Pack = 1)]
    public struct PhysiologicalDataBase_Ext1
    {
      public B450Comms.arrh_ecg_group ecg;
      public B450Comms.ecg_12_group ecg12;
      public unsafe fixed byte reserved[192];
    }

    [StructLayout(LayoutKind.Sequential, Size = 48, Pack = 1)]
    public struct arrh_ecg_group
    {
      public B450Comms.Group_Header hdr;
      public short hr;
      public short rr_time;
      public short pvc;
      public uint arrh_reserved;
      private unsafe fixed short reserved[16];
    }

    [StructLayout(LayoutKind.Sequential, Size = 30, Pack = 1)]
    public struct ecg_12_group
    {
      public B450Comms.Group_Header hdr;
      public short stI;
      public short stII;
      public short stIII;
      public short stAVL;
      public short stAVR;
      public short stAVF;
      public short stV1;
      public short stV2;
      public short stV3;
      public short stV4;
      public short stV5;
      public short stV6;
    }

    [StructLayout(LayoutKind.Sequential, Size = 270, Pack = 1)]
    public struct PhysiologicalDataBase_Ext2
    {
      public B450Comms.nmt2_group nmt2;
      public B450Comms.eeg_group eeg;
      public B450Comms.eeg_bis_group eeg_bis;
      public B450Comms.entropy_group ent;
      public B450Comms.entropy_group ent_rd;
      public unsafe fixed byte reserved1[13];
      public B450Comms.eeg2_group eeg2;
      public B450Comms.spi_group spi;
      public unsafe fixed byte reserved2[41];
    }

    [StructLayout(LayoutKind.Sequential, Size = 24, Pack = 1)]
    public struct nmt2_group
    {
      public B450Comms.Group_Header hdr;
      public short reserved;
      public short nmt_t1;
      public short nmt_t2;
      public short nmt_t3;
      public short nmt_t4;
      public short nmt_resv1;
      public short nmt_resv2;
      public short nmt_resv3;
      public short nmt_resv4;
    }

    [StructLayout(LayoutKind.Sequential, Size = 72, Pack = 1)]
    public struct eeg_group
    {
      public B450Comms.Group_Header hdr;
      public short femg;
      public B450Comms.eeg_channel eeg1;
      public B450Comms.eeg_channel eeg2;
      public B450Comms.eeg_channel eeg3;
      public B450Comms.eeg_channel eeg4;
    }

    [StructLayout(LayoutKind.Sequential, Size = 16, Pack = 1)]
    public struct eeg_channel
    {
      public short ampl;
      public short sef;
      public short mf;
      public short delta_proc;
      public short theta_proc;
      public short alpha_proc;
      public short beta_proc;
      public short bsr;
    }

    [StructLayout(LayoutKind.Sequential, Size = 16, Pack = 1)]
    public struct eeg_bis_group
    {
      public B450Comms.Group_Header hdr;
      public short bis;
      public short sqi_val;
      public short emg_val;
      public short sr_val;
      public short reserved;
    }

    [StructLayout(LayoutKind.Sequential, Size = 28, Pack = 1)]
    public struct entropy_group
    {
      public B450Comms.Group_Header hdr;
      public short eeg_ent;
      public short emg_ent;
      public short bsr_ent;
      private unsafe fixed short reserved[8];
    }

    [StructLayout(LayoutKind.Sequential, Size = 32, Pack = 1)]
    public struct eeg2_group
    {
      public B450Comms.Group_Header hdr;
      public byte common_reference;
      public byte montage_label_ch_1_m;
      public byte montage_label_ch_1_p;
      public byte montage_label_ch_2_m;
      public byte montage_label_ch_2_p;
      public byte montage_label_ch_3_m;
      public byte montage_label_ch_3_p;
      public byte montage_label_ch_4_m;
      public byte montage_label_ch_4_p;
      private byte res_byte;
      private unsafe fixed short reserved[8];
    }

    [StructLayout(LayoutKind.Sequential, Size = 16, Pack = 1)]
    public struct spi_group
    {
      public B450Comms.Group_Header hdr;
      public short spiVal;
      private unsafe fixed short reserved[4];
    }

    [StructLayout(LayoutKind.Sequential, Size = 270, Pack = 1)]
    public struct PhysiologicalDataBase_Ext3
    {
      public B450Comms.gasex_group gasex;
      public B450Comms.flow_vol_group2 flow_vol2;
      public B450Comms.bal_gas_group bal;
      public B450Comms.tono_group tono;
      public B450Comms.aa2_group aa2;
      private unsafe fixed byte reserved[154];
    }

    [StructLayout(LayoutKind.Sequential, Size = 14, Pack = 1)]
    public struct gasex_group
    {
      public B450Comms.Group_Header hdr;
      public short vo2;
      public short vco2;
      public short ee;
      public short rq;
    }

    [StructLayout(LayoutKind.Sequential, Size = 46, Pack = 1)]
    public struct flow_vol_group2
    {
      public B450Comms.Group_Header hdr;
      public short ipeep;
      public short pmean;
      public short raw;
      public short mv_insp;
      public short epeep;
      public short mv_spont;
      public short ie_ratio;
      public short insp_time;
      public short exp_time;
      public short static_compliance;
      public short static_pplat;
      public short static_peepe;
      public short static_peepi;
      public unsafe fixed short reserved[7];
    }

    [StructLayout(LayoutKind.Sequential, Size = 10, Pack = 1)]
    public struct bal_gas_group
    {
      public B450Comms.Group_Header hdr;
      public short et;
      public short fi;
    }

    [StructLayout(LayoutKind.Sequential, Size = 22, Pack = 1)]
    public struct tono_group
    {
      public B450Comms.Group_Header hdr;
      public short prco2;
      public short pr_et;
      public short pr_pa;
      public short pa_delay;
      public short phi;
      public short phi_delay;
      public short amb_press;
      public short cpma;
    }

    [StructLayout(LayoutKind.Sequential, Size = 24, Pack = 1)]
    public struct aa2_group
    {
      public B450Comms.Group_Header hdr;
      public short mac_age_sum;
      private unsafe fixed byte reserved[16];
    }

    public delegate void RawDataReceivedEventHandler(B450Comms sender, byte[] data);

    public delegate void RawDataTransmittedEventHandler(B450Comms sender, byte[] data);
  }
}
