// Decompiled with JetBrains decompiler
// Type: B450_Testbench.B450_Labview_Debug
// Assembly: B450_Labview_V2, Version=1.0.0.1, Culture=neutral, PublicKeyToken=null
// MVID: 83C7D531-E990-492D-9D70-D78678AED62E
// Assembly location: \\Mac\Home\Documents\RTD31DApp\data\B450_Labview_V2.dll

using System;
using System.ComponentModel;
using System.Drawing;
using System.Windows.Forms;

namespace B450_Testbench
{
  public class B450_Labview_Debug : Form
  {
    private bool active;
    private B450_Labview b450;
    private IContainer components;
    private Button button1;

    public B450_Labview_Debug(B450_Labview b450)
    {
      this.InitializeComponent();
      this.b450 = b450;
      this.active = false;
    }

    public new bool Active
    {
      get => this.active;
      set
      {
        if (value && !this.active)
          this.Show();
        else if (!value && this.active)
          this.Hide();
        this.active = value;
      }
    }

    private void button1_Click(object sender, EventArgs e)
    {
      if (this.b450 == null)
        return;
      this.Text = this.b450.Num_ECG_Waveform.ToString();
    }

    protected override void Dispose(bool disposing)
    {
      if (disposing && this.components != null)
        this.components.Dispose();
      base.Dispose(disposing);
    }

    private void InitializeComponent()
    {
      this.button1 = new Button();
      this.SuspendLayout();
      this.button1.Location = new Point(298, 132);
      this.button1.Name = "button1";
      this.button1.Size = new Size(75, 23);
      this.button1.TabIndex = 0;
      this.button1.Text = "button1";
      this.button1.UseVisualStyleBackColor = true;
      this.button1.Click += new EventHandler(this.button1_Click);
      this.AutoScaleDimensions = new SizeF(6f, 13f);
      this.AutoScaleMode = AutoScaleMode.Font;
      this.ClientSize = new Size(480, 285);
      this.Controls.Add((Control) this.button1);
      this.Name = nameof (B450_Labview_Debug);
      this.StartPosition = FormStartPosition.CenterScreen;
      this.Text = nameof (B450_Labview_Debug);
      this.ResumeLayout(false);
    }
  }
}
