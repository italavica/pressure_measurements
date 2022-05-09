import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import butter, lfilter, freqz,filtfilt
from functions import plot_exp,exp_analisys,PTT,plot_single,PS1_filter_10
from scipy.signal import find_peaks
from matplotlib.pyplot import plot, legend, show, grid, figure, savefig, title
import extract_data_27Apr22

s1,s2,s3,s4,s5,s6,s7,s8,s9,s10=extract_data_27Apr22.extract_data_6V()


def PTT_v1(s1,s2,s3,s4,s5,s6,s7,s8,s9,s10):

    PS1_1=s1['Voltage_1'][0:10400]
    PS1_2=s2['Voltage_1'][0:11000]
    PS1_3=s3['Voltage_1'][0:11000]
    PS1_4=s4['Voltage_1'][0:11000]
    PS1_5=s5['Voltage_1'][0:11000]
    PS1_6=s6['Voltage_1'][0:11000]
    PS1_7=s7['Voltage_1'][0:11000]
    PS1_8=s8['Voltage_1'][0:11000]
    PS1_9=s9['Voltage_1'][0:10830]
    PS1_10=s10['Voltage_1'][0:11000]

    PS2_1=s1['Voltage_2'][0:10400]
    PS2_2=s2['Voltage_2'][0:11000]
    PS2_3=s3['Voltage_2'][0:11000]
    PS2_4=s4['Voltage_2'][0:11000]
    PS2_5=s5['Voltage_2'][0:11000]
    PS2_6=s6['Voltage_2'][0:11000]
    PS2_7=s7['Voltage_2'][0:11000]
    PS2_8=s8['Voltage_2'][0:11000]
    PS2_9=s9['Voltage_2'][0:10830]
    PS2_10=s10['Voltage_2'][0:11000]


    PS1_filtered_1,PS1_filtered_2,PS1_filtered_3,PS1_filtered_4,PS1_filtered_5,PS1_filtered_6,PS1_filtered_7,PS1_filtered_8,PS1_filtered_9,PS1_filtered_10=PS1_filter_10(PS1_1,PS1_2,PS1_3,PS1_4,PS1_5,PS1_6,PS1_7,PS1_8,PS1_9,PS1_10,10,1000,6)
    PS2_filtered_1,PS2_filtered_2,PS2_filtered_3,PS2_filtered_4,PS2_filtered_5,PS2_filtered_6,PS2_filtered_7,PS2_filtered_8,PS2_filtered_9,PS2_filtered_10=PS1_filter_10(PS2_1,PS2_2,PS2_3,PS2_4,PS2_5,PS2_6,PS2_7,PS2_8,PS2_9,PS2_10,10,1000,6)
    l=10830
    fs=1000
    t= np.arange(0, l/fs, 1/fs)
    

    loc_PS1_1, _ = find_peaks(PS1_filtered_1, distance=900)
    loc_PS2_1, _ = find_peaks(PS2_filtered_1, distance=900)
    PTT_1= loc_PS2_1[0:10]-loc_PS1_1[0:10]
    mPTT_1=(np.average(PTT_1))/fs

    loc_PS1_2, _ = find_peaks(PS1_filtered_2, distance=900)
    loc_PS2_2, _ = find_peaks(PS2_filtered_2, distance=900)
    PTT_2= loc_PS2_2[0:10]-loc_PS1_2[0:10]
    mPTT_2=(np.average(PTT_2))/fs

    loc_PS1_3, _ = find_peaks(PS1_filtered_3, distance=900)
    loc_PS2_3, _ = find_peaks(PS2_filtered_3, distance=900)
    PTT_3= loc_PS2_3[0:10]-loc_PS1_3[0:10]
    mPTT_3=(np.average(PTT_3))/fs

    loc_PS1_4, _ = find_peaks(PS1_filtered_4, distance=900)
    loc_PS2_4, _ = find_peaks(PS2_filtered_4, distance=900)
    PTT_4= loc_PS2_4[0:10]-loc_PS1_4[0:10]
    mPTT_4=(np.average(PTT_4))/fs

    loc_PS1_5, _ = find_peaks(PS1_filtered_5, distance=900)
    loc_PS2_5, _ = find_peaks(PS2_filtered_5, distance=900)
    PTT_5= loc_PS2_5[0:10]-loc_PS1_5[0:10]
    mPTT_5=(np.average(PTT_5))/fs

    loc_PS1_6, _ = find_peaks(PS1_filtered_6, distance=900)
    loc_PS2_6, _ = find_peaks(PS2_filtered_6, distance=900)
    PTT_6= loc_PS2_6[0:10]-loc_PS1_6[0:10]
    mPTT_6=(np.average(PTT_6))/fs

    loc_PS1_7, _ = find_peaks(PS1_filtered_7, distance=900)
    loc_PS2_7, _ = find_peaks(PS2_filtered_7, distance=900)
    PTT_7= loc_PS2_7[0:10]-loc_PS1_7[0:10]
    mPTT_7=(np.average(PTT_7))/fs

    loc_PS1_8, _ = find_peaks(PS1_filtered_8, distance=900)
    loc_PS2_8, _ = find_peaks(PS2_filtered_8, distance=900)
    PTT_8= loc_PS2_8[0:10]-loc_PS1_8[0:10]
    mPTT_8=(np.average(PTT_8))/fs

    loc_PS1_9, _ = find_peaks(PS1_filtered_9, distance=900)
    loc_PS2_9, _ = find_peaks(PS2_filtered_9, distance=900)
    PTT_9= loc_PS2_9[0:10]-loc_PS1_9[0:10]
    mPTT_9=(np.average(PTT_9))/fs

    loc_PS1_10, _ = find_peaks(PS1_filtered_10, distance=900)
    loc_PS2_10, _ = find_peaks(PS2_filtered_10, distance=900)
    PTT_10= loc_PS2_10[0:10]-loc_PS1_10[0:10]
    mPTT_10=(np.average(PTT_10))/fs

    figure(figsize=(10,5))
    plot(t,PS1_9, 'g', linewidth=1.75,label='PS1')
    plot(t,PS1_filtered_9, 'g', linewidth=1.75,label='PS1')
    plot(loc_PS1_9/fs,PS1_filtered_9[loc_PS1_9], 'r*', linewidth=1.75)
    plot(t,PS2_filtered_9, 'b', linewidth=1.75,label='PS2')
    plot(loc_PS2_9/fs,PS2_filtered_9[loc_PS2_9], 'r*', linewidth=1.75)
    legend()
    title("Peaks PS1 and PS2")
    grid(True)
    show()

    # figure(figsize=(10,5))
    # plot(t,PS1_filtered_4, 'g', linewidth=1.75,label='PS1')
    # plot(loc_PS1_4/fs,PS1_filtered_4[loc_PS1_4], 'r*', linewidth=1.75)
    # plot(t,PS2_filtered_4, 'b', linewidth=1.75,label='PS2')
    # plot(loc_PS2_4/fs,PS2_filtered_4[loc_PS2_4], 'r*', linewidth=1.75)
    # legend()
    # title("Peaks PS1 and PS2")
    # grid(True)
    # show()

    
    mPTT=np.average([mPTT_1,mPTT_2,mPTT_3,mPTT_5,mPTT_6,mPTT_7,mPTT_8,mPTT_9,mPTT_10])
    sPTT=np.std([mPTT_1,mPTT_2,mPTT_3,mPTT_5,mPTT_6,mPTT_7,mPTT_8,mPTT_9,mPTT_10])
    print(PTT_1,PTT_2,PTT_3,PTT_4,PTT_5,PTT_6,PTT_7,PTT_8,PTT_9,PTT_10)
    return mPTT,sPTT
print('6 V')
s1_6V,s2_6V,s3_6V,s4_6V,s5_6V,s6_6V,s7_6V,s8_6V,s9_6V,s10_6V=extract_data_27Apr22.extract_data_6V()
mPTT_6V,sPTT_6V=PTT_v1(s1_6V,s2_6V,s3_6V,s4_6V,s5_6V,s6_6V,s7_6V,s8_6V,s9_6V,s10_6V)
print('7 V')
s1_7V,s2_7V,s3_7V,s4_7V,s5_7V,s6_7V,s7_7V,s8_7V,s9_7V,s10_7V=extract_data_27Apr22.extract_data_7V()
mPTT_7V,sPTT_7V=PTT_v1(s1_7V,s2_7V,s3_7V,s4_7V,s5_7V,s6_7V,s7_7V,s8_7V,s9_7V,s10_7V)
print('8 V')
s1_8V,s2_8V,s3_8V,s4_8V,s5_8V,s6_8V,s7_8V,s8_8V,s9_8V,s10_8V=extract_data_27Apr22.extract_data_8V()
mPTT_8V,sPTT_8V=PTT_v1(s1_8V,s2_8V,s3_8V,s4_8V,s5_8V,s6_8V,s7_8V,s8_8V,s9_8V,s10_8V)
print('9 V')
s1_9V,s2_9V,s3_9V,s4_9V,s5_9V,s6_9V,s7_9V,s8_9V,s9_9V,s10_9V=extract_data_27Apr22.extract_data_9V()
mPTT_9V,sPTT_9V=PTT_v1(s1_9V,s2_9V,s3_9V,s4_9V,s5_9V,s6_9V,s7_9V,s8_9V,s9_9V,s10_9V)
print('10 V')
s1_10V,s2_10V,s3_10V,s4_10V,s5_10V,s6_10V,s7_10V,s8_10V,s9_10V,s10_10V=extract_data_27Apr22.extract_data_10V()
mPTT_10V,sPTT_10V=PTT_v1(s1_10V,s2_10V,s3_10V,s4_10V,s5_10V,s6_10V,s7_10V,s8_10V,s9_10V,s10_10V)
print('11 V')
s1_11V,s2_11V,s3_11V,s4_11V,s5_11V,s6_11V,s7_11V,s8_11V,s9_11V,s10_11V=extract_data_27Apr22.extract_data_11V()
mPTT_11V,sPTT_11V=PTT_v1(s1_11V,s2_11V,s3_11V,s4_11V,s5_11V,s6_11V,s7_11V,s8_11V,s9_11V,s10_11V)
print('12 V')
s1_12V,s2_12V,s3_12V,s4_12V,s5_12V,s6_12V,s7_12V,s8_12V,s9_12V,s10_12V=extract_data_27Apr22.extract_data_12V()
mPTT_12V,sPTT_12V=PTT_v1(s1_12V,s2_12V,s3_12V,s4_12V,s5_12V,s6_12V,s7_12V,s8_12V,s9_12V,s10_12V)


PTT_std=[sPTT_6V,sPTT_7V,sPTT_8V,sPTT_9V,sPTT_10V,sPTT_11V,sPTT_12V]
PTT_voltages=[mPTT_6V,mPTT_7V,mPTT_8V,mPTT_9V,mPTT_10V,mPTT_11V,mPTT_12V]
voltages=[6,7,8,9,10,11,12]



plt.figure()
plt.errorbar(voltages, PTT_voltages, PTT_std, marker='s', mfc='red',
         mec='black', ms=8, mew=2,label='PTT')
plt.xticks(voltages) 
plt.title('PTT increasing voltage')
plt.xlabel('voltage (V)') 
plt.ylabel('PTT (sec)')
plt.legend()
plt.show()


