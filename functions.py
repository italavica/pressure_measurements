import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import find_peaks
from scipy.signal import butter, lfilter, freqz,filtfilt

def plot_single(df1):
    fs=1000
    l1=len(df1)
    t1= np.arange(0, l1/fs, 1/fs)
    plt.figure()
    #plt.plot(t1,df1['Voltage_0'], label='motor pump')
    plt.plot(t1,df1['Voltage_1'],label='PS1')
    plt.plot(t1,df1['Voltage_2'],label='PS2')
    #plt.plot(t1,df1['SBP'],label='SBP')
    #plt.plot(t1,df1['DBP'],label='DBP')
    #plt.plot(t1,df1['MBP'],label='MBP')
    plt.title('Tubular phantom pressure measurments experiment')
    plt.xlabel('time (sec)') 
    plt.ylabel('Amplitude')
    plt.legend()
    plt.show()

def plot_exp(df1,df2,df3,df4,df5):
    fs=1000

    l1=len(df1)
    l2=len(df2)
    l3=len(df3)
    l4=len(df4)
    l5=len(df5)

    t1= np.arange(0, l1/fs, 1/fs)
    t2= np.arange(0, l2/fs, 1/fs)
    t3= np.arange(0, l3/fs, 1/fs)
    t4= np.arange(0, l4/fs, 1/fs)
    t5= np.arange(0, l5/fs, 1/fs)

    plt.figure()
    plt.plot(t1,df1['Voltage_0'], label='motor pump')
    plt.plot(t1,df1['Voltage_1'],label='PS1')
    plt.plot(t1,df1['Voltage_2'],label='PS2')
    plt.plot(t1,df1['SBP'],label='SBP')
    plt.plot(t1,df1['DBP'],label='DBP')
    plt.plot(t1,df1['MBP'],label='MBP')
    plt.title('Tubular phantom pressure measurments experiment')
    plt.xlabel('time (sec)') 
    plt.ylabel('Amplitude')
    plt.legend()
    plt.show()

    # plt.figure()
    # plt.plot(t2,df2['Voltage_0'],t2,df2['Voltage_1'],t2,df2['Voltage_2'],t2,df2['SBP'],t2,df2['DBP'],t2,df2['MBP'])
    # plt.title('')
    # plt.xlabel('time (sec)') 
    # plt.ylabel('Amplitude')
    # plt.show()

    # plt.figure()
    # plt.plot(t3,df3['Voltage_0'],t3,df3['Voltage_1'],t3,df3['Voltage_2'],t3,df3['SBP'],t3,df3['DBP'],t3,df3['MBP'])
    # plt.title('')
    # plt.xlabel('time (sec)') 
    # plt.ylabel('Amplitude')
    # plt.show()

    # plt.figure()
    # plt.plot(t1,df1['Voltage_0'],t4,df4['Voltage_1'],t4,df4['Voltage_2'],t4,df4['SBP'],t4,df4['DBP'],t4,df4['MBP'])
    # plt.title('')
    # plt.xlabel('time (sec)') 
    # plt.ylabel('Amplitude')
    # plt.show()

    # plt.figure()
    # plt.plot(t5,df5['Voltage_0'],t5,df5['Voltage_1'],t5,df5['Voltage_2'],t5,df5['SBP'],t5,df5['DBP'],t5,df5['MBP'])
    # plt.title('')
    # plt.xlabel('time (sec)') 
    # plt.ylabel('Amplitude')
    # plt.show()

def exp_analisys(df1,df2,df3,df4,df5):

    loc_PS1_1, _ = find_peaks(df1['Voltage_1'], distance=900)
    loc_PS2_1, _ = find_peaks(df1['Voltage_2'], distance=900)
    MPS1_1=np.average( df1['Voltage_1'][loc_PS1_1])
    MPS2_1=np.average( df1['Voltage_2'][loc_PS2_1])

    loc_PS1_2, _ = find_peaks(df2['Voltage_1'], distance=900)
    loc_PS2_2, _ = find_peaks(df2['Voltage_2'], distance=900)
    MPS1_2=np.average( df2['Voltage_1'][loc_PS1_2])
    MPS2_2=np.average( df2['Voltage_2'][loc_PS2_2])

    loc_PS1_3, _ = find_peaks(df3['Voltage_1'], distance=900)
    loc_PS2_3, _ = find_peaks(df3['Voltage_2'], distance=900)
    MPS1_3=np.average( df3['Voltage_1'][loc_PS1_3])
    MPS2_3=np.average( df3['Voltage_2'][loc_PS2_3])

    plt.figure()
    plt.plot(df3['Voltage_1'],label='PS1')
    plt.plot(df3['Voltage_2'],label='PS2')
    plt.plot(loc_PS1_3, df3['Voltage_1'][loc_PS1_3], "x",label='peaks PS1')
    plt.plot(loc_PS2_3, df3['Voltage_2'][loc_PS2_3], "x",label='peaks PS2')
    plt.title('Tubular phantom pressure measurments experiment')
    plt.xlabel('time (sec)') 
    plt.ylabel('Amplitude')
    plt.legend()
    plt.show()

    loc_PS1_4, _ = find_peaks(df4['Voltage_1'], distance=900)
    loc_PS2_4, _ = find_peaks(df4['Voltage_2'], distance=900)
    MPS1_4=np.average( df4['Voltage_1'][loc_PS1_4])
    MPS2_4=np.average( df4['Voltage_2'][loc_PS2_4])

    loc_PS1_5, _ = find_peaks(df5['Voltage_1'], distance=900)
    loc_PS2_5, _ = find_peaks(df5['Voltage_2'], distance=900)
    MPS1_5=np.average( df5['Voltage_1'][loc_PS1_5])
    MPS2_5=np.average( df5['Voltage_2'][loc_PS2_5])

 
    mean_MPS1=np.average([MPS1_1,MPS1_2,MPS1_3,MPS1_4,MPS1_5])
    mean_MPS2=np.average([MPS2_1,MPS2_2,MPS2_3,MPS2_4,MPS2_5])


    std_MPS1=np.std([MPS1_1,MPS1_2,MPS1_3,MPS1_4,MPS1_5])
    std_MPS2=np.std([MPS2_1,MPS2_2,MPS2_3,MPS2_4,MPS2_5])


    mean_SBP=np.average([df1['SBP'][0],df2['SBP'][0],df3['SBP'][0],df4['SBP'][0],df5['SBP'][0]])
    mean_DBP=np.average([df1['DBP'][0],df2['DBP'][0],df3['DBP'][0],df4['DBP'][0],df5['DBP'][0]])
    mean_MBP=np.average([df1['MBP'][0],df2['MBP'][0],df3['MBP'][0],df4['MBP'][0],df5['MBP'][0]])

    std_SBP=np.std([df1['SBP'][0],df2['SBP'][0],df3['SBP'][0],df4['SBP'][0],df5['SBP'][0]])
    std_DBP=np.std([df1['DBP'][0],df2['DBP'][0],df3['DBP'][0],df4['DBP'][0],df5['DBP'][0]])
    std_MBP=np.std([df1['MBP'][0],df2['MBP'][0],df3['MBP'][0],df4['MBP'][0],df5['MBP'][0]])

    #print(mean_MPS1,std_MPS1,mean_MPS2,std_MPS2,mean_SBP,std_SBP,mean_DBP,std_DBP,mean_MBP,std_MBP)

    return mean_MPS1,std_MPS1,mean_MPS2,std_MPS2,mean_SBP,std_SBP,mean_DBP,std_DBP,mean_MBP,std_MBP

def PTT(df1,df2,df3,df4,df5):

    loc_PS1_1, _ = find_peaks(df1['Voltage_1'], distance=900)
    loc_PS2_1, _ = find_peaks(df1['Voltage_2'], distance=900)
    PTT_1= loc_PS2_1[0:4]-loc_PS1_1[0:4]
    mPTT_1=np.average(PTT_1)

    loc_PS1_2, _ = find_peaks(df2['Voltage_1'], distance=900)
    loc_PS2_2, _ = find_peaks(df2['Voltage_2'], distance=900)
    PTT_2= loc_PS2_2[0:4]-loc_PS1_2[0:4]
    mPTT_2=np.average(PTT_2)

    loc_PS1_3, _ = find_peaks(df3['Voltage_1'], distance=900)
    loc_PS2_3, _ = find_peaks(df3['Voltage_2'], distance=900)
    PTT_3= loc_PS2_3[0:4]-loc_PS1_3[0:4]
    mPTT_3=np.average(PTT_3)

    loc_PS1_4, _ = find_peaks(df4['Voltage_1'], distance=900)
    loc_PS2_4, _ = find_peaks(df4['Voltage_2'], distance=900)
    PTT_4= loc_PS2_4[0:4]-loc_PS1_4[0:4]
    mPTT_4=np.average(PTT_4)

    loc_PS1_5, _ = find_peaks(df5['Voltage_1'], distance=900)
    loc_PS2_5, _ = find_peaks(df5['Voltage_2'], distance=900)
    PTT_5= loc_PS2_5[0:4]-loc_PS1_5[0:4]
    mPTT_5=np.average(PTT_5)

    mPTT=np.average([mPTT_1,mPTT_2,mPTT_3,mPTT_5])
    sPTT=np.std([mPTT_1,mPTT_2,mPTT_3,mPTT_5])
    #print(PTT_1,PTT_2,PTT_3,PTT_4,PTT_5)
    return mPTT,sPTT

def extract_signal_freq(x):
  f=[]
  # compute DFT with optimized FFT
  w = np.fft.fft(x)
  # compute frequency associated
  # with coefficients
  freqs = np.fft.fftfreq(len(x))
  # extract frequencies associated with FFT values
  firstNegInd = np.argmax(freqs < 0)
  freqs = freqs[0:firstNegInd]
  w = 2 * w[0:firstNegInd]  # *2 because of magnitude of analytic signal
  for coef, freq in zip(w, freqs):
      if abs(coef)==max(abs(w)):
        f.append(freq)
  return f



def fftPlot(sig, dt=None, plot=True):
    # Here it's assumes analytic signal (real signal...) - so only half of the axis is required

    if dt is None:
        dt = 1
        t = np.arange(0, sig.shape[-1])
        xLabel = 'samples'
    else:
        t = np.arange(0, sig.shape[-1]) * dt
        xLabel = 'freq [Hz]'

    if sig.shape[0] % 2 != 0:
        warnings.warn("signal preferred to be even in size, autoFixing it...")
        t = t[0:-1]
        sig = sig[0:-1]
    # print("tshape",t.shape[0])
    sigFFT = np.fft.fft(sig) / t.shape[0]  # Divided by size t for coherent magnitude

    freq = np.fft.fftfreq(t.shape[0], d=dt)

    # Plot analytic signal - right half of frequence axis needed only...
    firstNegInd = np.argmax(freq < 0)
    freqAxisPos = freq[0:firstNegInd]
    sigFFTPos = 2 * sigFFT[0:firstNegInd]  # *2 because of magnitude of analytic signal

    if plot:
        plt.figure()
        plt.plot(freqAxisPos, np.abs(sigFFTPos))
        plt.xlabel(xLabel)
        plt.ylabel('mag')
        plt.title('Analytic FFT plot')
        plt.show()

    return sigFFTPos, freqAxisPos


def butter_lowpass(cutoff, fs, order=5):
    nyq = 0.5 * fs
    normal_cutoff = cutoff / nyq
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    return b, a



def butter_lowpass_filter(data, cutoff, fs, order=5):
    b, a = butter_lowpass(cutoff, fs, order=order)
    y = lfilter(b, a, data)
    return y



def PS1_filter(data,cutoff, fs, order):
    l=len(data)
    t= np.arange(0, l/fs, 1/fs)
    b, a = butter_lowpass(cutoff, fs, order)
    y = butter_lowpass_filter(data, cutoff, fs, order)
    y1 = filtfilt(b, a, data)

    return y1,t

def PS1_filter_5(d1,d2,d3,d4,d5,cutoff, fs, order):

    b, a = butter_lowpass(cutoff, fs, order)
    y1 = filtfilt(b, a, d1)
    y2 = filtfilt(b, a, d2)
    y3 = filtfilt(b, a, d3)
    y4 = filtfilt(b, a, d4)
    y5 = filtfilt(b, a, d5)

    return y1,y2,y3,y4,y5

def PS1_filter_10(d1,d2,d3,d4,d5,d6,d7,d8,d9,d10,cutoff, fs, order):

    b, a = butter_lowpass(cutoff, fs, order)
    y1 = filtfilt(b, a, d1)
    y2 = filtfilt(b, a, d2)
    y3 = filtfilt(b, a, d3)
    y4 = filtfilt(b, a, d4)
    y5 = filtfilt(b, a, d5)
    y6 = filtfilt(b, a, d6)
    y7 = filtfilt(b, a, d7)
    y8 = filtfilt(b, a, d8)
    y9 = filtfilt(b, a, d9)
    y10 = filtfilt(b, a, d10)

    return y1,y2,y3,y4,y5,y6,y7,y8,y9,y10

