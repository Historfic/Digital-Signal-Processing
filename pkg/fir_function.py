import tkinter as tk
import customtkinter
from tkinter import filedialog, messagebox
import os
import numpy as np
import librosa
import cv2
from PIL import Image, ImageTk

# Import FIR Audio functions
from .FIR_audio import apply_fir_filter, plot_audio

# Import FIR Image functions
from .FIR_image import apply_image_filter, plot_images

class FIRApplication(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("FIR Filter Application")
        self.geometry("600x600")

        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("dark-blue")

        # Variables
        self.file_path = ""
        self.file_type = tk.StringVar(value="audio")
        
        # Configure grid layout
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)

        # Create Widgets
        self.create_widgets()
    
    def create_widgets(self):
        # Title Label
        title_label = customtkinter.CTkLabel(master=self, text="FIR Filter Application", font=("Century Gothic", 50, "bold"))
        title_label.grid(row=0, column=0, columnspan=2, pady=20, padx=20, sticky="n")

        # Upload Audio Button
        self.upload_audio_button = customtkinter.CTkButton(self, text='Upload Audio', command=self.upload_audio, font=("Roboto", 30, "bold"),height=200)
        self.upload_audio_button.grid(row=1, column=0, padx=5, pady=5, sticky="ew")

        # Upload Image Button
        self.upload_image_button = customtkinter.CTkButton(self, text='Upload Image', command=self.upload_image, font=("Roboto", 30, "bold"),height=200)
        self.upload_image_button.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

        # Apply Audio Filter Button
        self.apply_audio_filter_button = customtkinter.CTkButton(self, text="Apply Audio Filter", command=self.apply_audio_filter, font=("Roboto", 30, "bold"),height=200)
        self.apply_audio_filter_button.grid(row=2, column=0, padx=5, pady=5, sticky="ew")

        # Apply Image Filter Button
        self.apply_image_filter_button = customtkinter.CTkButton(self, text="Apply Image Filter", command=self.apply_image_filter, font=("Roboto", 30, "bold"),height=200)
        self.apply_image_filter_button.grid(row=2, column=1, padx=5, pady=5, sticky="ew")

        # Back Button
        self.back_button = customtkinter.CTkButton(self, text="Back", command=self.back, font=("Roboto", 30, "bold"), height=75)
        self.back_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5, sticky="ew")

    def upload_image(self):
        try:
            file_types = [("Image files", "*.jpg *.jpeg *.png *.bmp *.gif")]
            self.file_path = filedialog.askopenfilename(filetypes=file_types)
            if self.file_path:
                messagebox.showinfo("Selected File", f"Image file selected: {os.path.basename(self.file_path)}")
        except Exception as e:
            print(f'An error has occurred during upload_image: {e}')

    def upload_audio(self):
        try:
            file_types = [("Audio files", "*.wav;*.mp3")]
            self.file_path = filedialog.askopenfilename(filetypes=file_types)
            if self.file_path:
                messagebox.showinfo("Selected File", f"Audio file selected: {os.path.basename(self.file_path)}")
        except Exception as e:
            messagebox.showerror("Error", f"An error has occurred during upload_audio: {e}")

    def apply_audio_filter(self):
        if not self.file_path:
            messagebox.showerror("Error", "No file selected.")
            return
        
        try:
            audio, sr = librosa.load(self.file_path, sr=None)
            filtered_audio = apply_fir_filter(audio, sr)
            plot_audio(audio, filtered_audio, sr)
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred during audio filtering: {e}")

    def apply_image_filter(self):
        if not self.file_path:
            messagebox.showerror("Error", "No file selected.")
            return
        try:
            image = cv2.imread(self.file_path)
            filtered_image, inverse_image, edge_image = apply_image_filter(image, brightness=150, kernel_size=5, inverse=True, edge_detector=True)
            plot_images(image, filtered_image, inverse_image, edge_image)
        except Exception as e:
            print(f"An error has occurred during image filtering: {e}")
            messagebox.showerror("Error", f"An error has occurred during image filtering: {e}")

    def back(self):
        self.destroy()

def run_fir():
    app = FIRApplication()
    app.mainloop()


