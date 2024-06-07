import tkinter as tk
from tkinter import *
from tkinter import filedialog, messagebox
import cv2
import matplotlib.pyplot as plt
import customtkinter

def apply_high_pass_filter(file_path):
    image = cv2.imread(file_path, cv2.IMREAD_COLOR)
    if image is None:
        messagebox.showerror("Error", "Failed to read the image.")
        return

    # Convert to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian blur
    blurred_image = cv2.GaussianBlur(gray_image, (21, 21), 0)

    # Subtract the blurred image from the original image
    high_pass_image = cv2.subtract(gray_image, blurred_image)

    # Normalize the result
    normalized_high_pass = cv2.normalize(high_pass_image, None, 0, 255, cv2.NORM_MINMAX)

    return normalized_high_pass

def apply_low_pass_filter(file_path):
    image = cv2.imread(file_path, cv2.IMREAD_COLOR)
    if image is None:
        messagebox.showerror("Error", "Failed to read the image.")
        return

    # Convert to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian blur for low-pass filtering
    low_pass = cv2.GaussianBlur(gray_image, (21, 21), 0)

    return low_pass

def upload_photo_and_display(file_path):
    # Verify the image is read correctly
    image = cv2.imread(file_path, cv2.IMREAD_COLOR)
    if image is not None:
        # Display the original image
        plt.figure(figsize=(12, 6))
        plt.subplot(1, 3, 1)
        plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
        plt.title("Original Image")
        plt.axis('off')

        # Process the image with high-pass filter
        high_pass_image = apply_high_pass_filter(file_path)
        plt.subplot(1, 3, 2)
        plt.imshow(high_pass_image, cmap='gray')
        plt.title("High-Pass Filtered Image")
        plt.axis('off')

        # Process the image with low-pass filter
        low_pass_image = apply_low_pass_filter(file_path)
        plt.subplot(1, 3, 3)
        plt.imshow(low_pass_image, cmap='gray')
        plt.title("Low-Pass Filtered Image")
        plt.axis('off')

        plt.show()
    else:
        messagebox.showerror("Error", "Failed to upload image.")

def selector():
    file_types = [("Image files", "*.jpg *.jpeg *.png *.bmp *.gif")]
    file_path = filedialog.askopenfilename(filetypes=file_types)
    if file_path:
        upload_photo_and_display(file_path)

def close():
    root.destroy()

def run_high_pass_to_low_pass():
    global root
    root = customtkinter.CTk()
    root.title('High Pass to Low Pass Filter')
    root.geometry("300x200")
    selector_button = customtkinter.CTkButton(master=root, text="Select Image", command=selector)
    selector_button.place(relx=0.5, rely=0.5, anchor=CENTER)
    root.mainloop()

if __name__ == '__main__':
    run_high_pass_to_low_pass()
