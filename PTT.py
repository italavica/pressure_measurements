import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import butter, lfilter, freqz,filtfilt
from functions import plot_exp,exp_analisys,PTT,plot_single,PS1_filter_5
from scipy.signal import find_peaks
#from matplotlib.pyplot import plot, legend, show, grid, figure, savefig, title
import extract_data

s1,s2,s3,s4,s5=extract_data.extract_data_18ml()

""" figure(figsize=(10,5))
plot(T_PS1,PS1, 'b', linewidth=1.75, alpha=0.75)
plot(T_PS1,PS1_filtered, 'r', linewidth=1.75)

        'PS1 filtered'),
        loc='best')
title("PS1 signal filtered")
grid(True)
show()

figure(figsize=(10,5))
plot(T_PS2,PS2, 'b', linewidth=1.75, alpha=0.75)
plot(T_PS2,PS2_filtered, 'r', linewidth=1.75)

legend(('PS2 noisy signal',
        'PS2 filtered'),
        loc='best')
title("PS2 signal filtered")
grid(True)
show() """

def mean_MBP(s1,s2,s3,s4,s5):
    mean_MBP=np.average([s1['MBP'][500],s2['MBP'][500],s3['MBP'][500],s4['MBP'][500],s5['MBP'][500]])
    std_MBP=np.std([s1['MBP'][500],s2['MBP'][500],s3['MBP'][500],s4['MBP'][500],s5['MBP'][500]])
    return mean_MBP, std_MBP


def PTT_v1(s1,s2,s3,s4,s5):

    PS1_1=s1['Voltage_1'][0:5000]
    PS1_2=s2['Voltage_1'][0:5000]
    PS1_3=s3['Voltage_1'][0:5000]
    PS1_4=s4['Voltage_1'][0:5000]
    PS1_5=s5['Voltage_1'][0:5000]

    PS2_1=s1['Voltage_2'][0:5000]
    PS2_2=s2['Voltage_2'][0:5000]
    PS2_3=s3['Voltage_2'][0:5000]
    PS2_4=s4['Voltage_2'][0:5000]
    PS2_5=s5['Voltage_2'][0:5000]


    PS1_filtered_1,PS1_filtered_2,PS1_filtered_3,PS1_filtered_4,PS1_filtered_5=PS1_filter_5(PS1_1,PS1_2,PS1_3,PS1_4,PS1_5,10,1000,6)

    PS2_filtered_1,PS2_filtered_2,PS2_filtered_3,PS2_filtered_4,PS2_filtered_5=PS1_filter_5(PS2_1,PS2_2,PS2_3,PS2_4,PS2_5,10,1000,6)
    l=5000
    fs=1000
    t= np.arange(0, l/fs, 1/fs)
    

    loc_PS1_1, _ = find_peaks(PS1_filtered_1, distance=900)
    loc_PS2_1, _ = find_peaks(PS2_filtered_1, distance=900)
    PTT_1= loc_PS2_1[0:4]-loc_PS1_1[0:4]
    mPTT_1=(np.average(PTT_1))/fs

    loc_PS1_2, _ = find_peaks(PS1_filtered_2, distance=900)
    loc_PS2_2, _ = find_peaks(PS2_filtered_2, distance=900)
    PTT_2= loc_PS2_2[0:4]-loc_PS1_2[0:4]
    mPTT_2=(np.average(PTT_2))/fs

    loc_PS1_3, _ = find_peaks(PS1_filtered_3, distance=900)
    loc_PS2_3, _ = find_peaks(PS2_filtered_3, distance=900)
    PTT_3= loc_PS2_3[0:4]-loc_PS1_3[0:4]
    mPTT_3=(np.average(PTT_3))/fs

    loc_PS1_4, _ = find_peaks(PS1_filtered_4, distance=900)
    loc_PS2_4, _ = find_peaks(PS2_filtered_4, distance=900)
    PTT_4= loc_PS2_4[0:4]-loc_PS1_4[0:4]
    mPTT_4=(np.average(PTT_4))/fs

    loc_PS1_5, _ = find_peaks(PS1_filtered_5, distance=900)
    loc_PS2_5, _ = find_peaks(PS2_filtered_5, distance=900)
    PTT_5= loc_PS2_5[0:4]-loc_PS1_5[0:4]
    mPTT_5=(np.average(PTT_5))/fs



    # figure(figsize=(10,5))
    # plot(t,PS1_filtered_3, 'g', linewidth=1.75,label='PS1')
    # plot(loc_PS1_3/fs,PS1_filtered_3[loc_PS1_3], 'r*', linewidth=1.75)
    # plot(t,PS2_filtered_3, 'b', linewidth=1.75,label='PS2')
    # plot(loc_PS2_3/fs,PS2_filtered_3[loc_PS2_3], 'r*', linewidth=1.75)
    # legend()
    # title("Peaks PS1 and PS2")
    # grid(True)
    # show()

    
    mPTT=np.average([mPTT_1,mPTT_2,mPTT_3,mPTT_5])
    sPTT=np.std([mPTT_1,mPTT_2,mPTT_3,mPTT_5])
    print(PTT_1,PTT_2,PTT_3,PTT_4,PTT_5)
    return mPTT,sPTT


s1_18,s2_18,s3_18,s4_18,s5_18=extract_data.extract_data_18ml()
mPTT_18,sPTT_18=PTT_v1(s1_18,s2_18,s3_18,s4_18,s5_18)
mean_MBP_18, std_MBP_18= mean_MBP(s1_18,s2_18,s3_18,s4_18,s5_18)

s1_28,s2_28,s3_28,s4_28,s5_28=extract_data.extract_data_28ml()
mPTT_28,sPTT_28=PTT_v1(s1_28,s2_28,s3_28,s4_28,s5_28)
mean_MBP_28, std_MBP_28= mean_MBP(s1_28,s2_28,s3_28,s4_28,s5_28)

s1_38,s2_38,s3_38,s4_38,s5_38=extract_data.extract_data_38ml()
mPTT_38,sPTT_38=PTT_v1(s1_38,s2_38,s3_38,s4_38,s5_38)
mean_MBP_38, std_MBP_38= mean_MBP(s1_38,s2_38,s3_38,s4_38,s5_38)

s1_48,s2_48,s3_48,s4_48,s5_48=extract_data.extract_data_48ml()
mPTT_48,sPTT_48=PTT_v1(s1_48,s2_48,s3_48,s4_48,s5_48)
mean_MBP_48, std_MBP_48= mean_MBP(s1_48,s2_48,s3_48,s4_48,s5_48)

s1_5v2,s2_5v2,s3_5v2,s4_5v2,s5_5v2=extract_data.extract_data_5V2()
mPTT_5v2,sPTT_5v2=PTT_v1(s1_5v2,s2_5v2,s3_5v2,s4_5v2,s5_5v2)
mean_MBP_5v2, std_MBP_5v2= mean_MBP(s1_5v2,s2_5v2,s3_5v2,s4_5v2,s5_5v2)

s1_7v2,s2_7v2,s3_7v2,s4_7v2,s5_7v2=extract_data.extract_data_7V2()
mPTT_7v2,sPTT_7v2=PTT_v1(s1_7v2,s2_7v2,s3_7v2,s4_7v2,s5_7v2)
mean_MBP_7v2, std_MBP_7v2= mean_MBP(s1_7v2,s2_7v2,s3_7v2,s4_7v2,s5_7v2)





PTT_std=[sPTT_18,sPTT_28,sPTT_38,sPTT_48]
MBP_std=[std_MBP_18,std_MBP_28,std_MBP_38,std_MBP_48]

PTT_volumes=[mPTT_18,mPTT_28,mPTT_38,mPTT_48]
MBP_volumes=[mean_MBP_18,mean_MBP_28,mean_MBP_38,mean_MBP_48]


PTT_std_v=[sPTT_5v2,sPTT_28,sPTT_7v2]
MBP_std_v=[std_MBP_5v2,std_MBP_28,std_MBP_7v2]
MBP_voltage=[mean_MBP_5v2,mean_MBP_28,mean_MBP_7v2]

PTT_voltage=[mPTT_5v2,mPTT_28,mPTT_7v2]

volumes=[18,28,38,48]
voltages=[5.2,6.2,7.2]

plt.figure()
plt.errorbar(voltages, PTT_voltage, PTT_std_v, marker='s', mfc='red',
         mec='black', ms=8, mew=2,label='PTT')
plt.xticks(voltages) 
plt.title('PTT increasing voltage')
plt.xlabel('voltage (V)') 
plt.ylabel('Pressure (mmHg)')
plt.legend()
plt.show()

plt.figure()
plt.errorbar(voltages, MBP_voltage, MBP_std_v, marker='s', mfc='blue',
         mec='black', ms=8, mew=2,label='MBP')
plt.xticks(voltages) 
plt.title('MBP increasing voltage')
plt.xlabel('voltage (V)') 
plt.ylabel('Pressure (mmHg)')
plt.legend()
plt.show()


plt.figure()
plt.errorbar(volumes, MBP_volumes, MBP_std, marker='s', mfc='blue',
         mec='black', ms=8, mew=2,label='MBP')
plt.xticks(volumes) 
plt.title('MBP increasing volume')
plt.xlabel('volume (ml)') 
plt.ylabel('Pressure (mmHg)')
plt.legend()
plt.show()

plt.figure()
plt.errorbar(volumes, PTT_volumes, PTT_std, marker='s', mfc='red',
         mec='black', ms=8, mew=2,label='PTT')
plt.xticks(volumes) 
plt.title('PTT increasing volume')
plt.xlabel('volume (ml)') 
plt.ylabel('Pressure (mmHg)')
plt.legend()
plt.show()

fig, ax1 = plt.subplots()

color = 'tab:green'
ax1.set_xlabel('volume (ml)')
ax1.set_ylabel('PTT (sec)', color=color)
ax1.errorbar(volumes, PTT_volumes, PTT_std, marker='s',color=color, mfc=color,
         mec='black', ms=8, mew=2,label='PTT')
ax1.tick_params(axis='y', labelcolor=color)


ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

color = 'tab:blue'
ax2.set_ylabel('MBP (mmHg)', color=color)  # we already handled the x-label with ax1
ax2.errorbar(volumes, MBP_volumes, MBP_std, marker='s', color=color, mfc=color,
         mec='black', ms=8, mew=2,label='MBP')
ax2.tick_params(axis='y', labelcolor=color)
 
plt.title('PTT and MBP increasing volume')

fig.tight_layout()  # otherwise the right y-label is slightly clipped
plt.xticks(volumes) 


plt.show()

fig, ax1 = plt.subplots()

color = 'tab:green'
ax1.set_xlabel('voltage (V)')
ax1.set_ylabel('PTT (sec)', color=color)
ax1.errorbar(voltages, PTT_voltage, PTT_std_v, marker='s',color=color, mfc=color,
         mec='black', ms=8, mew=2,label='PTT')
ax1.tick_params(axis='y', labelcolor=color)


ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

color = 'tab:blue'
ax2.set_ylabel('MBP (mmHg)', color=color)  # we already handled the x-label with ax1
ax2.errorbar(voltages, MBP_voltage, MBP_std_v, marker='s', color=color, mfc=color,
         mec='black', ms=8, mew=2,label='MBP')
ax2.tick_params(axis='y', labelcolor=color)
 
plt.title('PTT and MBP increasing voltage')

fig.tight_layout()  # otherwise the right y-label is slightly clipped
plt.xticks(voltages) 


plt.show()