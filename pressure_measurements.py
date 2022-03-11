import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from functions import plot_exp,exp_analisys
from scipy.signal import find_peaks

#extract data

#18 ml @ 6.2 V
df_18_1 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\Phantom_measurements_9_03_22\backup_10.csv")
df_18_2 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\Phantom_measurements_9_03_22\backup_11.csv")
df_18_3 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\Phantom_measurements_9_03_22\backup_12.csv")
df_18_4 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\Phantom_measurements_9_03_22\backup_13.csv")
df_18_5 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\Phantom_measurements_9_03_22\backup_14.csv")

#28 ml @ 6.2 V
df_28_1 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\Phantom_measurements_9_03_22\backup_25.csv")
df_28_2 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\Phantom_measurements_9_03_22\backup_26.csv")
df_28_3 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\Phantom_measurements_9_03_22\backup_27.csv")
df_28_4 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\Phantom_measurements_9_03_22\backup_28.csv")
df_28_5 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\Phantom_measurements_9_03_22\backup_29.csv")

#38 ml @ 6.2 V
df_38_1 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\Phantom_measurements_9_03_22\backup_15.csv")
df_38_2 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\Phantom_measurements_9_03_22\backup_16.csv")
df_38_3 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\Phantom_measurements_9_03_22\backup_17.csv")
df_38_4 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\Phantom_measurements_9_03_22\backup_18.csv")
df_38_5 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\Phantom_measurements_9_03_22\backup_19.csv")

#48 ml @ 6.2 V
df_48_1 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\Phantom_measurements_9_03_22\backup_20.csv")
df_48_2 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\Phantom_measurements_9_03_22\backup_21.csv")
df_48_3 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\Phantom_measurements_9_03_22\backup_22.csv")
df_48_4 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\Phantom_measurements_9_03_22\backup_23.csv")
df_48_5 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\Phantom_measurements_9_03_22\backup_24.csv")

# Changing Voltage
#28 ml @ 7.2 V
df_28_7_1 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\Phantom_measurements_9_03_22\backup_30.csv")
df_28_7_2 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\Phantom_measurements_9_03_22\backup_31.csv")
df_28_7_3 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\Phantom_measurements_9_03_22\backup_32.csv")
df_28_7_4 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\Phantom_measurements_9_03_22\backup_33.csv")
df_28_7_5 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\Phantom_measurements_9_03_22\backup_34.csv")
df_28_7_6 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\Phantom_measurements_9_03_22\backup_35.csv")

#28 ml @ 5.2 V
df_28_5_1 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\Phantom_measurements_9_03_22\backup_37.csv")
df_28_5_2 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\Phantom_measurements_9_03_22\backup_38.csv")
df_28_5_3 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\Phantom_measurements_9_03_22\backup_39.csv")
df_28_5_4 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\Phantom_measurements_9_03_22\backup_40.csv")
df_28_5_5 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\Phantom_measurements_9_03_22\backup_41.csv")

print(len(df_18_1),len(df_18_2),len(df_18_3),len(df_18_4),len(df_18_5))
print(len(df_28_1),len(df_28_2),len(df_28_3),len(df_28_4),len(df_28_5))
print(len(df_38_1),len(df_38_2),len(df_38_3),len(df_38_4),len(df_38_5))
print(len(df_48_1),len(df_48_2),len(df_48_3),len(df_48_4),len(df_48_5))
print(len(df_28_7_1),len(df_28_7_2),len(df_28_7_3),len(df_28_7_4),len(df_28_7_5),len(df_28_7_6))
print(len(df_28_5_1),len(df_28_5_2),len(df_28_5_3),len(df_28_5_4),len(df_28_5_5))

df_48_1['Voltage_2'][4159:4162] = (df_48_1['Voltage_2'][4159]+df_48_1['Voltage_2'][4162])/2
df_48_3['Voltage_1'][1700:1703] = (df_48_3['Voltage_1'][1700]+df_48_3['Voltage_1'][1703])/2
df_28_5_1['Voltage_2'][3510:3513]= (df_28_5_1['Voltage_2'][3510]+df_28_5_1['Voltage_2'][3513])/2
df_28_5_1['Voltage_1'][3510:3513]= (df_28_5_1['Voltage_1'][3510]+df_28_5_1['Voltage_1'][3513])/2

#plot_exp(df_18_1[0:5000],df_18_2[0:5000],df_18_3[1750:6750],df_18_4[0:5000],df_18_5[0:5000])
#plot_exp(df_28_1[0:5000],df_28_2[0:5000],df_28_3[0:5000],df_28_4[0:5000],df_28_5[0:5000])
#plot_exp(df_38_1[0:5000],df_38_2[0:5000],df_38_3[0:5000],df_38_4[2150:7150],df_38_5[0:5000])
#plot_exp(df_48_1[0:5000],df_48_2[0:5000],df_48_3[0:5000],df_48_4[0:5000],df_48_5[0:5000])
#plot_exp(df_28_7_1[0:5000],df_28_7_2[0:5000],df_28_7_3[0:5000],df_28_7_4[0:5000],df_28_7_5[0:5000])
#plot_exp(df_28_5_1[0:5000],df_28_5_2[0:5000],df_28_5_3[0:5000],df_28_5_4[0:5000],df_28_5_5[0:5000])


#volume variation

mean_MPS1_18,std_MPS1_18,mean_MPS2_18,std_MPS2_18,mean_SBP_18,std_SBP_18,mean_DBP_18,std_DBP_18,mean_MBP_18,std_MBP_18 = exp_analisys(df_18_1[0:5000],df_18_2[0:5000],df_18_3[0:5000],df_18_4[0:5000],df_18_5[0:5000])
mean_MPS1_28,std_MPS1_28,mean_MPS2_28,std_MPS2_28,mean_SBP_28,std_SBP_28,mean_DBP_28,std_DBP_28,mean_MBP_28,std_MBP_28 = exp_analisys(df_28_1[0:5000],df_28_2[0:5000],df_28_3[0:5000],df_28_4[0:5000],df_28_5[0:5000])
mean_MPS1_38,std_MPS1_38,mean_MPS2_38,std_MPS2_38,mean_SBP_38,std_SBP_38,mean_DBP_38,std_DBP_38,mean_MBP_38,std_MBP_38 = exp_analisys(df_38_1[0:5000],df_38_2[0:5000],df_38_3[0:5000],df_38_4[0:5000],df_38_5[0:5000])
mean_MPS1_48,std_MPS1_48,mean_MPS2_48,std_MPS2_48,mean_SBP_48,std_SBP_48,mean_DBP_48,std_DBP_48,mean_MBP_48,std_MBP_48 = exp_analisys(df_48_1[0:5000],df_48_2[0:5000],df_48_3[0:5000],df_48_4[0:5000],df_48_5[0:5000])
volumes=[18,28,38,48]

#voltage variation

mean_MPS1_28_7,std_MPS1_28_7,mean_MPS2_28_7,std_MPS2_28_7,mean_SBP_28_7,std_SBP_28_7,mean_DBP_28_7,std_DBP_28_7,mean_MBP_28_7,std_MBP_28_7 = exp_analisys(df_28_7_1[0:5000],df_28_7_2[0:5000],df_28_7_3[0:5000],df_28_7_4[0:5000],df_28_7_5[0:5000])
mean_MPS1_28_5,std_MPS1_28_5,mean_MPS2_28_5,std_MPS2_28_5,mean_SBP_28_5,std_SBP_28_5,mean_DBP_28_5,std_DBP_28_5,mean_MBP_28_5,std_MBP_28_5 = exp_analisys(df_28_5_1[0:5000],df_28_5_2[0:5000],df_28_5_3[0:5000],df_28_5_4[0:5000],df_28_5_5[0:5000])
voltages=[5.2,6.2,7.2]

mean_MPS1 = [mean_MPS1_18, mean_MPS1_28, mean_MPS1_38, mean_MPS1_48]
std_MPS1 = [std_MPS1_18, std_MPS1_28, std_MPS1_38, std_MPS1_48]

mean_MPS2 = [mean_MPS2_18, mean_MPS2_28, mean_MPS2_38, mean_MPS2_48]
std_MPS2 = [std_MPS2_18, std_MPS2_28, std_MPS2_38, std_MPS2_48]

mean_SBP = [mean_SBP_18, mean_SBP_28, mean_SBP_38, mean_SBP_48]
std_SBP = [std_SBP_18, std_SBP_28, std_SBP_38, std_SBP_48]

mean_DBP = [mean_DBP_18, mean_DBP_28, mean_DBP_38, mean_DBP_48]
std_DBP = [std_DBP_18, std_DBP_28, std_DBP_38, std_DBP_48]

mean_MBP = [mean_MBP_18, mean_MBP_28, mean_MBP_38, mean_MBP_48]
std_MBP = [std_MBP_18, std_MBP_28, std_MBP_38, std_MBP_48]

mean_PS1_V=[mean_MPS1_28_5,mean_MPS1_28,mean_MPS1_28_7]
mean_PS2_V=[mean_MPS2_28_5,mean_MPS2_28,mean_MPS2_28_7]
mean_SBP_V=[mean_SBP_28_5,mean_SBP_28,mean_SBP_28_7]
mean_DBP_V=[mean_DBP_28_5,mean_DBP_28,mean_DBP_28_7]
mean_MBP_V=[mean_MBP_28_5,mean_MBP_28,mean_MBP_28_7]

std_PS1_V=[std_MPS1_28_5,std_MPS1_28,std_MPS1_28_7]
std_PS2_V=[std_MPS2_28_5,std_MPS2_28,std_MPS2_28_7]
std_SBP_V=[std_SBP_28_5,std_SBP_28,std_SBP_28_7]
std_DBP_V=[std_DBP_28_5,std_DBP_28,std_DBP_28_7]
std_MBP_V=[std_MBP_28_5,std_MBP_28,std_MBP_28_7]

plt.figure()
plt.errorbar(volumes, mean_MPS1, std_MPS1, marker='s', mfc='red',
         mec='black', ms=8, mew=2,label='PS1')
plt.errorbar(volumes, mean_MPS2, std_MPS2, marker='s', mfc='blue',
         mec='black', ms=8, mew=2,label='PS2')
plt.errorbar(volumes, mean_SBP, std_SBP, marker='s', mfc='green',
         mec='black', ms=8, mew=2,label='SBP')
plt.errorbar(volumes, mean_DBP, std_DBP, marker='s', mfc='brown',
         mec='black', ms=8, mew=2,label='DBP')
plt.errorbar(volumes, mean_MBP, std_MBP, marker='s', mfc='purple',
         mec='black', ms=8, mew=2,label='MBP')
plt.xticks(volumes) 
plt.title('Phantom pressure measurements at different volumes @6.2 V')
plt.xlabel('volume (ml)') 
plt.ylabel('Pressure (mmHg)')
plt.legend()
plt.show()

plt.figure()
plt.errorbar(voltages, mean_PS1_V, std_PS1_V, marker='s', mfc='red',
         mec='black', ms=8, mew=2,label='PS1')
plt.errorbar(voltages, mean_PS2_V, std_PS2_V, marker='s', mfc='blue',
         mec='black', ms=8, mew=2,label='PS2')
plt.errorbar(voltages, mean_SBP_V, std_SBP_V, marker='s', mfc='green',
         mec='black', ms=8, mew=2,label='SBP')
plt.errorbar(voltages, mean_DBP_V, std_DBP_V, marker='s', mfc='brown',
         mec='black', ms=8, mew=2,label='DBP')
plt.errorbar(voltages, mean_MBP_V, std_MBP_V, marker='s', mfc='purple',
         mec='black', ms=8, mew=2,label='MBP')
plt.xticks(voltages) 
plt.title('Phantom pressure measurements at different voltages @28 ml')
plt.xlabel('voltage (V)') 
plt.ylabel('Pressure (mmHg)')
plt.legend()
plt.show()