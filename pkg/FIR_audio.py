import numpy as np
import scipy.signal as signal
import matplotlib.pyplot as plt
import librosa

def apply_fir_filter(audio, sampling_rate):
    cutoff_freq = 4000  # Cutoff frequency
    numtaps = 101  # Number of taps in FIR filter

    def design_fir_filter(Fs, Fc, numtaps):
        nyquist = Fs / 2  # Normalize cutoff frequency
        normalized_cutoff = Fc / nyquist
        h = signal.firwin(numtaps, normalized_cutoff)  # FIR filter using firwin
        return h

    # Design the FIR Filter for the given sampling rate
    fir_coeff = design_fir_filter(sampling_rate, cutoff_freq, numtaps)
    filtered_audio = signal.convolve(audio, fir_coeff, mode='same') / np.sum(fir_coeff)
    return filtered_audio

def plot_audio(audio, filtered_audio, sampling_rate):
    if audio is None or filtered_audio is None:
        return

    # Time array for plotting
    time = np.arange(len(audio)) / sampling_rate

    # Plotting
    plt.figure(figsize=(10, 8))

    plt.subplot(3, 1, 1)
    plt.title('Original Audio Signal')
    plt.plot(time, audio, label='Original Signal')
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.legend()
    plt.grid()

    plt.subplot(3, 1, 2)
    plt.title('Filtered Audio Signal')
    plt.plot(time, filtered_audio, label='Filtered Signal', color='orange')
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.legend()
    plt.grid()

    plt.subplot(3, 1, 3)
    plt.title('Original and Filtered Audio Signals')
    plt.plot(time, audio, label='Original Signal')
    plt.plot(time, filtered_audio, label='Filtered Signal', color='orange')
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.legend()
    plt.grid()

    plt.tight_layout()
    plt.show()
