import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import butter, lfilter, freqz,filtfilt
from functions import plot_exp,exp_analisys,PTT,plot_single,PS1_filter_10
from scipy.signal import find_peaks
from matplotlib.pyplot import plot, legend, show, grid, figure, savefig, title
import extract_data_27Apr22

s1,s2,s3,s4,s5,s6,s7,s8,s9,s10=extract_data_27Apr22.extract_data_10ml()

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

    loc_PS2_1, _ = find_peaks(PS2_filtered_1, distance=900)

    loc_PS2_2, _ = find_peaks(PS2_filtered_2, distance=900)

    loc_PS2_3, _ = find_peaks(PS2_filtered_3, distance=900)

    loc_PS2_4, _ = find_peaks(PS2_filtered_4, distance=900)

    loc_PS2_5, _ = find_peaks(PS2_filtered_5, distance=900)

    loc_PS2_6, _ = find_peaks(PS2_filtered_6, distance=900)

    loc_PS2_7, _ = find_peaks(PS2_filtered_7, distance=900)

    loc_PS2_8, _ = find_peaks(PS2_filtered_8, distance=900)

    loc_PS2_9, _ = find_peaks(PS2_filtered_9, distance=900)

    loc_PS2_10, _ = find_peaks(PS2_filtered_10, distance=900)


    mPS2_1=np.average(PS2_filtered_1[loc_PS2_1])
    mPS2_2=np.average(PS2_filtered_2[loc_PS2_2])
    mPS2_3=np.average(PS2_filtered_3[loc_PS2_3])
    mPS2_4=np.average(PS2_filtered_4[loc_PS2_4])
    mPS2_5=np.average(PS2_filtered_5[loc_PS2_5])
    mPS2_6=np.average(PS2_filtered_6[loc_PS2_6])
    mPS2_7=np.average(PS2_filtered_7[loc_PS2_7])
    mPS2_8=np.average(PS2_filtered_8[loc_PS2_8])
    mPS2_9=np.average(PS2_filtered_9[loc_PS2_9])
    mPS2_10=np.average(PS2_filtered_10[loc_PS2_10])

    # figure(figsize=(10,5))
    # plot(t,PS2_filtered_6, 'b', linewidth=1.75,label='PS2')
    # plot(loc_PS2_6/fs,PS2_filtered_6[loc_PS2_6], 'r*', linewidth=1.75)
    # legend()
    # title("Peaks PS2")
    # grid(True)
    # show()



    std_PS2=np.std([mPS2_1,mPS2_2,mPS2_3,mPS2_4,mPS2_5,mPS2_6,mPS2_7,mPS2_8,mPS2_9,mPS2_10])
    mean_PS2=np.average([mPS2_1,mPS2_2,mPS2_3,mPS2_4,mPS2_5,mPS2_6,mPS2_7,mPS2_8,mPS2_9,mPS2_10])

    print(mPS2_1,mPS2_2,mPS2_3,mPS2_4,mPS2_5,mPS2_6,mPS2_7,mPS2_8,mPS2_9,mPS2_10)

    return std_PS2,mean_PS2

s1_10ml,s2_10ml,s3_10ml,s4_10ml,s5_10ml,s6_10ml,s7_10ml,s8_10ml,s9_10ml,s10_10ml=extract_data_27Apr22.extract_data_10ml()
sPS2_10ml,mPS2_10ml=mPS2(s1_10ml,s2_10ml,s3_10ml,s4_10ml,s5_10ml,s6_10ml,s7_10ml,s8_10ml,s9_10ml,s10_10ml)

s1_15ml,s2_15ml,s3_15ml,s4_15ml,s5_15ml,s6_15ml,s7_15ml,s8_15ml,s9_15ml,s10_15ml=extract_data_27Apr22.extract_data_15ml()
sPS2_15ml,mPS2_15ml=mPS2(s1_15ml,s2_15ml,s3_15ml,s4_15ml,s5_15ml,s6_15ml,s7_15ml,s8_15ml,s9_15ml,s10_15ml)

s1_20ml,s2_20ml,s3_20ml,s4_20ml,s5_20ml,s6_20ml,s7_20ml,s8_20ml,s9_20ml,s10_20ml=extract_data_27Apr22.extract_data_20ml()
sPS2_20ml,mPS2_20ml,=mPS2(s1_20ml,s2_20ml,s3_20ml,s4_20ml,s5_20ml,s6_20ml,s7_20ml,s8_20ml,s9_20ml,s10_20ml)

s1_25ml,s2_25ml,s3_25ml,s4_25ml,s5_25ml,s6_25ml,s7_25ml,s8_25ml,s9_25ml,s10_25ml=extract_data_27Apr22.extract_data_25ml()
sPS2_25ml,mPS2_25ml=mPS2(s1_25ml,s2_25ml,s3_25ml,s4_25ml,s5_25ml,s6_25ml,s7_25ml,s8_25ml,s9_25ml,s10_25ml)

s1_30ml,s2_30ml,s3_30ml,s4_30ml,s5_30ml,s6_30ml,s7_30ml,s8_30ml,s9_30ml,s10_30ml=extract_data_27Apr22.extract_data_30ml()
sPS2_30ml,mPS2_30ml=mPS2(s1_30ml,s2_30ml,s3_30ml,s4_30ml,s5_30ml,s6_30ml,s7_30ml,s8_30ml,s9_30ml,s10_30ml)

s1_35ml,s2_35ml,s3_35ml,s4_35ml,s5_35ml,s6_35ml,s7_35ml,s8_35ml,s9_35ml,s10_35ml=extract_data_27Apr22.extract_data_35ml()
sPS2_35ml,mPS2_35ml=mPS2(s1_35ml,s2_35ml,s3_35ml,s4_35ml,s5_35ml,s6_35ml,s7_35ml,s8_35ml,s9_35ml,s10_35ml)

s1_40ml,s2_40ml,s3_40ml,s4_40ml,s5_40ml,s6_40ml,s7_40ml,s8_40ml,s9_40ml,s10_40ml=extract_data_27Apr22.extract_data_40ml()
sPS2_40ml,mPS2_40ml=mPS2(s1_40ml,s2_40ml,s3_40ml,s4_40ml,s5_40ml,s6_40ml,s7_40ml,s8_40ml,s9_40ml,s10_40ml)

s1_45ml,s2_45ml,s3_45ml,s4_45ml,s5_45ml,s6_45ml,s7_45ml,s8_45ml,s9_45ml,s10_45ml=extract_data_27Apr22.extract_data_45ml()
sPS2_45ml,mPS2_45ml=mPS2(s1_45ml,s2_45ml,s3_45ml,s4_45ml,s5_45ml,s6_45ml,s7_45ml,s8_45ml,s9_45ml,s10_45ml)

s1_50ml,s2_50ml,s3_50ml,s4_50ml,s5_50ml,s6_50ml,s7_50ml,s8_50ml,s9_50ml,s10_50ml=extract_data_27Apr22.extract_data_50ml()
sPS2_50ml,mPS2_50ml=mPS2(s1_50ml,s2_50ml,s3_50ml,s4_50ml,s5_50ml,s6_50ml,s7_50ml,s8_50ml,s9_50ml,s10_50ml)

s1_55ml,s2_55ml,s3_55ml,s4_55ml,s5_55ml,s6_55ml,s7_55ml,s8_55ml,s9_55ml,s10_55ml=extract_data_27Apr22.extract_data_55ml()
sPS2_55ml,mPS2_55ml=mPS2(s1_55ml,s2_55ml,s3_55ml,s4_55ml,s5_55ml,s6_55ml,s7_55ml,s8_55ml,s9_55ml,s10_55ml)

PS2_std=[sPS2_10ml,sPS2_15ml,sPS2_20ml,sPS2_25ml,sPS2_30ml,sPS2_35ml,sPS2_40ml,sPS2_45ml,sPS2_50ml,sPS2_55ml]
PS2_volumes=[mPS2_10ml,mPS2_15ml,mPS2_20ml,mPS2_25ml,mPS2_30ml,mPS2_35ml,mPS2_40ml,mPS2_45ml,mPS2_50ml,mPS2_55ml]

volumes=[10,15,20,25,30,35,40,45,50,55]

plt.figure()
plt.errorbar(volumes, PS2_volumes, PS2_std, marker='s', mfc='red',
         mec='black', ms=8, mew=2,label='PS2')
plt.xticks(volumes) 
plt.title('PS2 increasing volume')
plt.xlabel('volume (ml)') 
plt.ylabel('PS2 (mmHg)')
plt.legend()
plt.show()


