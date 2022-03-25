import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from functions import plot_exp,exp_analisys,PTT,plot_single,extract_signal_freq,fftPlot
from scipy.signal import find_peaks

df_18_1 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\Phantom_measurements_9_03_22\backup_10.csv")

plot_single(df_18_1[0:5000])

F= extract_signal_freq(df_18_1['Voltage_1'])

print(F)

fftPlot(df_18_1['Voltage_1'], dt=1/1000, plot=True)