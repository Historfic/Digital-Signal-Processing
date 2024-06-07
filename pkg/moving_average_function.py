import tkinter as tk
from tkinter import ttk
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def movingAverageFilter(csv_file, window_size):
    """
    This function is gets the csv file data and calculate the filtered signal into average signal
    """

    # reads the  csv file as pandas dataframe
    sensor_data = pd.read_csv(csv_file, header=None)
    x = np.asarray(sensor_data[0])
    y = np.asarray(sensor_data[1])

    # calculating the cumulative sum of the sensor data
    cumsum = np.cumsum(np.insert(y, 0, 0))

    # caclulating the filtered signal
    filtered_y = (cumsum[window_size:] -
                  cumsum[:-window_size]) / float(window_size)
    filtered_x = x[window_size - 1:]

    return x, y, filtered_x, filtered_y


# visualisation function
def visualize(x, y, filtered_x, filtered_y, window_size):
    """
    Use a window to display the filter and unfiltered waves
    """
    fig, ax = plt.subplots()
    plt.title('Moving Average Filter Using Sensor Data Noise)')
    plt.plot(x, y, label='unfiltered')
    plt.plot(filtered_x, filtered_y, label='filtered')
    plt.xlabel("x-axis")
    plt.ylabel("y-axis")
    plt.legend()
    plt.show()


def run_moving_average():
    window_size = 100

    file_data = r'resources\sensor_data.csv'

    x, y, filtered_x, filtered_y = movingAverageFilter(
        file_data, window_size)

    return visualize(x, y, filtered_x, filtered_y, window_size)


if __name__ == '__main__':
    run_moving_average()

