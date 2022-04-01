import pandas as pd
#import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import butter, lfilter, freqz,filtfilt
from functions import plot_exp,exp_analisys,PTT,plot_single,extract_signal_freq,fftPlot,butter_lowpass,butter_lowpass_filter
from scipy.signal import find_peaks
from matplotlib.pyplot import plot, legend, show, grid, figure, savefig, title

df_18_1 = pd.read_csv (r"C:\Users\ezxiaav\Documents\pressure_measurements\Data_experiments\Phantom_measurements_9_03_22\backup_10.csv")

plot_single(df_18_1[0:5000])

F= extract_signal_freq(df_18_1['Voltage_1'])

print(F)

fftPlot(df_18_1['Voltage_1'], dt=1/1000, plot=True)

# Filter requirements.
order = 6
fs = 1000       # sample rate, Hz
cutoff = 10  # desired cutoff frequency of the filter, Hz

# Get the filter coefficients so we can check its frequency response.
b, a = butter_lowpass(cutoff, fs, order)

""" # Plot the frequency response.
w, h = freqz(b, a, worN=8000)
plt.subplot(2, 1, 1)
plt.plot(0.5*fs*w/np.pi, np.abs(h), 'b')
plt.plot(cutoff, 0.5*np.sqrt(2), 'ko')
plt.axvline(cutoff, color='k')
plt.xlim(0, 0.5*fs)
plt.title("Lowpass Filter Frequency Response")
plt.xlabel('Frequency [Hz]')
plt.grid() """

# Filter of PPG signal
# First make some data to be filtered.
data=df_18_1['Voltage_1']
l=len(df_18_1['Voltage_1'])
t= np.arange(0, l/fs, 1/fs)
# "Noisy" data.  We want to recover the 1.2 Hz signal from this.

# Filter the data, and plot both the original and filtered signals.
y = butter_lowpass_filter(data, cutoff, fs, order)

""" plt.subplot(2, 1, 2)
plt.plot(t, data, 'b-', label='data')
plt.plot(t, y, 'g-', linewidth=2, label='filtered data')
plt.xlabel('Time [sec]')
plt.grid()
plt.legend()

plt.subplots_adjust(hspace=0.35)
plt.show() """

y1 = filtfilt(b, a, data)


# Make the plot.
figure(figsize=(10,5))
plot(t, data, 'b', linewidth=1.75, alpha=0.75)
plot(t, y, 'r', linewidth=1.75)
plot(t, y1, 'k', linewidth=1.75)
legend(('PS1 noisy signal',
        'Signal after LPF',
        'Signal after  phase-shift correction'),
        loc='best')
title("PS1 signal filtered")
grid(True)
show()