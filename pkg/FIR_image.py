from PIL import Image
import cv2
from matplotlib import pyplot as plt


def apply_image_filter(image, brightness, kernel_size, inverse=False, edge_detector=False):
    if image is None:
        raise ValueError("No image provided for filtering.")

    # Apply brightness adjustment
    filtered_image = cv2.convertScaleAbs(image, alpha=brightness / 100)

    # Ensure kernel size is odd
    if kernel_size % 2 == 0:
        kernel_size += 1
    # Apply Gaussian blur
    filtered_image = cv2.GaussianBlur(filtered_image, (kernel_size, kernel_size), 0)

    # Apply inverse filter if requested
    if inverse:
        inverse_image = cv2.bitwise_not(filtered_image)
    else:
        inverse_image = None

    # Apply edge detection if requested
    if edge_detector:
        edge_image = cv2.Canny(filtered_image, 100, 200)
    else:
        edge_image = None

    return filtered_image, inverse_image, edge_image

def plot_images(original_image, filtered_image, inverse_image, edge_image):
    if original_image is None or filtered_image is None or inverse_image is None or edge_image is None:
        raise ValueError("One of the images is None, cannot plot images.")

    plt.figure(figsize=(10, 5))

    plt.subplot(1, 4, 1)
    plt.title('Original Image')
    plt.imshow(cv2.cvtColor(original_image, cv2.COLOR_BGR2RGB))
    plt.axis('off')

    plt.subplot(1, 4, 2)
    plt.title('Filtered Image')
    plt.imshow(cv2.cvtColor(filtered_image, cv2.COLOR_BGR2RGB))
    plt.axis('off')

    plt.subplot(1, 4, 3)
    plt.title('Inverse Image')
    plt.imshow(cv2.cvtColor(inverse_image, cv2.COLOR_BGR2RGB))
    plt.axis('off')

    plt.subplot(1, 4, 4)
    plt.title('Edge Detection')
    plt.imshow(edge_image, cmap='gray')
    plt.axis('off')

    plt.tight_layout()
    plt.show()

