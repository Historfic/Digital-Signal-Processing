import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk

def generate_analog_signal(x, frequency, amplitude, phase):
    analog_signal = amplitude * np.sin(2 * np.pi * frequency * x + phase)
    return analog_signal

def generate_square_wave(x, frequency, amplitude, phase):
    period = 1 / frequency
    digital_signal = np.zeros_like(x)
    for i, t in enumerate(x):
        t_shifted = t - phase
        t_mod_period = t_shifted % period
        if t_mod_period < period / 2:
            digital_signal[i] = amplitude
        else:
            digital_signal[i] = -amplitude
    return digital_signal

def plot_signals(root):
    x = np.linspace(0, 4 * np.pi, 1000)  # Start x at 0
    frequency = 1
    amplitude = 1
    phase = 0

    analog_signal = generate_analog_signal(x, frequency, amplitude, phase)
    digital_signal = generate_square_wave(x, frequency, amplitude, phase)

    fig, axs = plt.subplots(2)
    plt.tight_layout(pad=3.0)

    fig.suptitle('Analog and Digital Signals')

    axs[0].plot(x, analog_signal)
    axs[0].set_title('Analog Signal')
    axs[0].set_xlabel('Time')
    axs[0].set_ylabel('Amplitude')
    axs[0].legend()
    axs[0].grid(True)  # Add grid to the analog signal plot

    axs[1].plot(x, digital_signal)
    axs[1].set_title('Digital Signal')
    axs[1].set_xlabel('Time')
    axs[1].set_ylabel('Amplitude')
    axs[1].legend()
    axs[1].grid(True)  # Add grid to the digital signal plot

    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

def run_adc():
    root = tk.Tk()
    root.title('Analog and Digital Signals')
    root.geometry('800x600')

    plot_signals(root)

    root.mainloop()

if __name__ == "__main__":
    run_adc()
