import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

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