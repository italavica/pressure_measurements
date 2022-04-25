import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import butter, lfilter, freqz,filtfilt
from functions import plot_exp,exp_analisys,PTT,plot_single,PS1_filter_10
from scipy.signal import find_peaks
from matplotlib.pyplot import plot, legend, show, grid, figure, savefig, title
import extract_data_21Apr22

s1,s2,s3,s4,s5,s6,s7,s8,s9,s10=extract_data_21Apr22.extract_data_10ml()

MBP_10ml=[55,65,64,67,75,78,63,66,63,73]
mean_MBP_10ml=np.average(MBP_10ml)
std_MBP_10ml=np.std(MBP_10ml)

MBP_15ml=[65,69,59,54,62,73,67,63,64,70]
mean_MBP_15ml=np.average(MBP_15ml)
std_MBP_15ml=np.std(MBP_15ml)

MBP_20ml=[75,65,71,63,60,63,59,61,87,71]
mean_MBP_20ml=np.average(MBP_20ml)
std_MBP_20ml=np.std(MBP_20ml)

MBP_25ml=[67,60,74,69,58,59,62,68,61,56]
mean_MBP_25ml=np.average(MBP_25ml)
std_MBP_25ml=np.std(MBP_25ml)

MBP_30ml=[59,60,71,62,68,70,73,55,64,70]
mean_MBP_30ml=np.average(MBP_30ml)
std_MBP_30ml=np.std(MBP_30ml)

MBP_35ml=[58,75,71,73,69,69,62,66,69,66]
mean_MBP_35ml=np.average(MBP_35ml)
std_MBP_35ml=np.std(MBP_35ml)

MBP_40ml=[59,57,59,61,59,54,65,49,57,60]
mean_MBP_40ml=np.average(MBP_40ml)
std_MBP_40ml=np.std(MBP_40ml)

MBP_45ml=[66,71,70,69,64,67,68,65,87,73]
mean_MBP_45ml=np.average(MBP_45ml)
std_MBP_45ml=np.std(MBP_45ml)

MBP_50ml=[71,74,76,73,76,77,69,77,73,65]
mean_MBP_50ml=np.average(MBP_50ml)
std_MBP_50ml=np.std(MBP_50ml)

MBP_55ml=[65,70,70,67,66,78,71,69,65,68]
mean_MBP_55ml=np.average(MBP_55ml)
std_MBP_55ml=np.std(MBP_55ml)

def mPS2(s1,s2,s3,s4,s5,s6,s7,s8,s9,s10):

    PS2_1=s1['Voltage_2'][0:11000]
    PS2_2=s2['Voltage_2'][0:11000]
    PS2_3=s3['Voltage_2'][0:11000]
    PS2_4=s4['Voltage_2'][0:11000]
    PS2_5=s5['Voltage_2'][0:11000]
    PS2_6=s6['Voltage_2'][0:10000]
    PS2_7=s7['Voltage_2'][0:11000]
    PS2_8=s8['Voltage_2'][0:11000]
    PS2_9=s9['Voltage_2'][0:11000]
    PS2_10=s10['Voltage_2'][0:11000]

    PS2_filtered_1,PS2_filtered_2,PS2_filtered_3,PS2_filtered_4,PS2_filtered_5,PS2_filtered_6,PS2_filtered_7,PS2_filtered_8,PS2_filtered_9,PS2_filtered_10=PS1_filter_10(PS2_1,PS2_2,PS2_3,PS2_4,PS2_5,PS2_6,PS2_7,PS2_8,PS2_9,PS2_10,10,1000,6)
    l=10000
    fs=1000
    t= np.arange(0, l/fs, 1/fs)

    mPS2_1=np.average(PS2_filtered_1)
    mPS2_2=np.average(PS2_filtered_2)
    mPS2_3=np.average(PS2_filtered_3)
    mPS2_4=np.average(PS2_filtered_4)
    mPS2_5=np.average(PS2_filtered_5)
    mPS2_6=np.average(PS2_filtered_6)
    mPS2_7=np.average(PS2_filtered_7)
    mPS2_8=np.average(PS2_filtered_8)
    mPS2_9=np.average(PS2_filtered_9)
    mPS2_10=np.average(PS2_filtered_10)

    std_PS2=np.std([mPS2_1,mPS2_2,mPS2_3,mPS2_4,mPS2_5,mPS2_6,mPS2_7,mPS2_8,mPS2_9,mPS2_10])
    mean_PS2=np.average([mPS2_1,mPS2_2,mPS2_3,mPS2_4,mPS2_5,mPS2_6,mPS2_7,mPS2_8,mPS2_9,mPS2_10])

    return std_PS2,mean_PS2
s1_10ml,s2_10ml,s3_10ml,s4_10ml,s5_10ml,s6_10ml,s7_10ml,s8_10ml,s9_10ml,s10_10ml=extract_data_21Apr22.extract_data_10ml()
mPS2_10ml,sPS2_10ml=mPS2(s1_10ml,s2_10ml,s3_10ml,s4_10ml,s5_10ml,s6_10ml,s7_10ml,s8_10ml,s9_10ml,s10_10ml)
