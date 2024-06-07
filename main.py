import tkinter as tk
import customtkinter
from pkg.adc_function import run_adc
from pkg.fir_function import run_fir
from pkg.moving_average_function import run_moving_average
from pkg.High_pass_to_Low_pass import run_high_pass_to_low_pass

# Main application window
class DSPApplication(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("dark-blue")

        self.title("Digital Signal Processing")
        self.geometry("600x600")

        # Configure grid layout
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)

        # Title Label
        title_label = customtkinter.CTkLabel(master=self, text="Digital Signal Processing \n Application", font=("Century Gothic", 41, "bold"))
        title_label.grid(row=0, column=0, columnspan=2, pady=40, padx=40, sticky="n")

        # Button to open ADC window
        adc_button = customtkinter.CTkButton(master=self, text="Analog to Digital \n Conversion \n (ADC)", font=("Roboto", 30, "bold"),height=200, command=run_adc)
        adc_button.grid(row=1, column=0, padx=5, pady=5, sticky="ew")

        # Button to open FIR Filter window
        fir_button = customtkinter.CTkButton(master=self, text="FIR Filter \n for \n Audio and Image", font=("Roboto", 30, "bold"), height=200, command=run_fir)
        fir_button.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

        # Button to open Moving Average Filter window
        moving_average_button = customtkinter.CTkButton(master=self, text="Moving Average \n Filter", font=("Roboto", 30, "bold"), height=200, command=run_moving_average)
        moving_average_button.grid(row=2, column=0, padx=5, pady=5, sticky="ew")

        # Button to open High-pass to Low-pass Filter Conversion window
        filter_conversion_button = customtkinter.CTkButton(master=self, text="High-pass \n to \n Low-pass \n Filter Conversion", font=("Roboto", 30, "bold"), height=200, command=run_high_pass_to_low_pass)
        filter_conversion_button.grid(row=2, column=1, padx=5, pady=5, sticky="ew")

# Run the application
if __name__ == "__main__":
    app = DSPApplication()
    app.mainloop()
