// Decompiled with JetBrains decompiler
// Type: B450_Testbench.ECG_Values
// Assembly: B450_Labview_V2, Version=1.0.0.1, Culture=neutral, PublicKeyToken=null
// MVID: 83C7D531-E990-492D-9D70-D78678AED62E
// Assembly location: \\Mac\Home\Documents\RTD31DApp\data\B450_Labview_V2.dll

namespace B450_Testbench
{
  public struct ECG_Values
  {
    public short HR_Primary;
    public HR_Source HR_Source;
    public short HeartRate;
    public short HeartRate_Max;
    public short HeartRate_Min;
    public bool Asystole;
    public bool Noise;
    public bool Artifact;
    public bool Learning;
    public bool Channel1Off;
    public bool Channel2Off;
    public bool Channel3Off;
    public bool ECGLeadsOff;
    public bool RespLeadsOff;
  }
}
