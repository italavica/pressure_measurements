import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import find_peaks

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
    plt.plot(t1,df1['Voltage_0'],t1,df1['Voltage_1'],t1,df1['Voltage_2'],t1,df1['SBP'],t1,df1['DBP'],t1,df1['MBP'])
    plt.title('')
    plt.xlabel('time (sec)') 
    plt.ylabel('Amplitude')
    plt.show()

    plt.figure()
    plt.plot(t2,df2['Voltage_0'],t2,df2['Voltage_1'],t2,df2['Voltage_2'],t2,df2['SBP'],t2,df2['DBP'],t2,df2['MBP'])
    plt.title('')
    plt.xlabel('time (sec)') 
    plt.ylabel('Amplitude')
    plt.show()

    plt.figure()
    plt.plot(t3,df3['Voltage_0'],t3,df3['Voltage_1'],t3,df3['Voltage_2'],t3,df3['SBP'],t3,df3['DBP'],t3,df3['MBP'])
    plt.title('')
    plt.xlabel('time (sec)') 
    plt.ylabel('Amplitude')
    plt.show()

    plt.figure()
    plt.plot(t1,df1['Voltage_0'],t4,df4['Voltage_1'],t4,df4['Voltage_2'],t4,df4['SBP'],t4,df4['DBP'],t4,df4['MBP'])
    plt.title('')
    plt.xlabel('time (sec)') 
    plt.ylabel('Amplitude')
    plt.show()

    plt.figure()
    plt.plot(t5,df5['Voltage_0'],t5,df5['Voltage_1'],t5,df5['Voltage_2'],t5,df5['SBP'],t5,df5['DBP'],t5,df5['MBP'])
    plt.title('')
    plt.xlabel('time (sec)') 
    plt.ylabel('Amplitude')
    plt.show()

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

    plt.plot(df3['Voltage_1'])
    plt.plot(loc_PS1_3, df3['Voltage_1'][loc_PS1_3], "x")
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

    print(mean_MPS1,std_MPS1,mean_MPS2,std_MPS2,mean_SBP,std_SBP,mean_DBP,std_DBP,mean_MBP,std_MBP)

    return mean_MPS1,std_MPS1,mean_MPS2,std_MPS2,mean_SBP,std_SBP,mean_DBP,std_DBP,mean_MBP,std_MBP

