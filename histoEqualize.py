import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

def histogram_equalization(image_path):
    # Read the image
    image = Image.open(image_path)
    
    # Convert image to grayscale if it's not already
    if image.mode != 'L':
        image = image.convert('L')
    
    # Convert image to numpy array
    image_array = np.array(image)
    
    # Calculate histogram
    hist, bins = np.histogram(image_array.flatten(), bins=256, range=(0, 256))
    
    # Calculate cumulative distribution function (CDF)
    cdf = hist.cumsum()
    
    # Normalize CDF to range [0, 255]
    cdf_normalized = ((cdf - cdf.min()) * 255) / (cdf.max() - cdf.min())
    
    # Interpolate the CDF to get the equalized pixel values
    equalized_image = np.interp(image_array.flatten(), bins[:-1], cdf_normalized).reshape(image_array.shape)
    
    # Convert to uint8 (0-255)
    equalized_image = equalized_image.astype(np.uint8)
    
    return equalized_image

def plot_histogram_equalized_image(image_path):
    # Perform histogram equalization
    equalized_image = histogram_equalization(image_path)
    
    # Display original and equalized images
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))
    
    # Display original image
    original_image = Image.open(image_path)
    ax1.imshow(original_image, cmap='gray')
    ax1.set_title('Original Image')
    ax1.axis('off')
    
    # Display equalized image
    ax2.imshow(equalized_image, cmap='gray')
    ax2.set_title('Equalized Image')
    ax2.axis('off')
    
    plt.tight_layout()
    plt.show()

# Specify the path to the image
image_path = "/home/ani/Desktop/test.png"

# Plot histogram equalized image
plot_histogram_equalized_image(image_path)
