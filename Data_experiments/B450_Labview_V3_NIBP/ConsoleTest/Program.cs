// Decompiled with JetBrains decompiler
// Type: ConsoleTest.Program
// Assembly: B450_Labview_V2, Version=1.0.0.1, Culture=neutral, PublicKeyToken=null
// MVID: 83C7D531-E990-492D-9D70-D78678AED62E
// Assembly location: \\Mac\Home\Documents\RTD31DApp\data\B450_Labview_V2.dll

using B450_Testbench;
using System;
using System.Threading;

namespace ConsoleTest
{
  public class Program
  {
    [STAThread]
    public static void Main(string[] args)
    {
      B450_Labview b450Labview = new B450_Labview("COM36");
      if (b450Labview.Good)
      {
        Console.WriteLine("Press key to STOP.");
        while (!Console.KeyAvailable)
        {
          if (b450Labview.Has_Errors)
          {
            Console.WriteLine(b450Labview.Next_Error);
            break;
          }
          if (b450Labview.Has_ECG_Values)
          {
            ECG_Values nextEcgValues = b450Labview.Next_ECG_Values;
            Console.WriteLine("ECG: " + nextEcgValues.Channel1Off.ToString() + ", " + nextEcgValues.ECGLeadsOff.ToString() + ", " + nextEcgValues.RespLeadsOff.ToString());
          }
          Thread.Sleep(100);
        }
        Console.ReadKey(true);
      }
      else
        Console.WriteLine("Failed to start.");
      b450Labview.Dispose();
    }

    public static string ValidateDataFormatString(
      object value,
      double decimalshift,
      bool rounddata)
    {
      int int32 = Convert.ToInt32(value);
      double a = Convert.ToDouble(value) * decimalshift;
      return int32 >= -32001 ? (rounddata ? Math.Round(a) : a).ToString() : "-";
    }

    public static string GetTimestamp()
    {
      DateTime now = DateTime.Now;
      return now.ToShortDateString() + ", " + now.ToLongTimeString() + "." + now.Millisecond.ToString("000");
    }
  }
}
