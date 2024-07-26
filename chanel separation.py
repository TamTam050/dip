import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

def separate_channels(image_path):
    # Read the image
    image = Image.open(image_path)
    
    # Convert image to numpy array
    image_array = np.array(image)
    
    # Separate color channels
    red_channel = image_array[:, :, 0]  # Red channel
    green_channel = image_array[:, :, 1]  # Green channel
    blue_channel = image_array[:, :, 2]  # Blue channel
    
    return red_channel, green_channel, blue_channel

def plot_channels(red_channel, green_channel, blue_channel):
    # Create subplots to display each channel
    fig, (ax1, ax2, ax3, ax4) = plt.subplots(1, 4, figsize=(15, 5))
    
    # Display original image
    ax1.imshow(np.array([red_channel, green_channel, blue_channel]).transpose(1, 2, 0))
    ax1.set_title('Original Image')
    ax1.axis('off')
    
    # Display red channel
    ax2.imshow(red_channel, cmap='gray')
    ax2.set_title('Red Channel')
    ax2.axis('off')
    
    # Display green channel
    ax3.imshow(green_channel, cmap='gray')
    ax3.set_title('Green Channel')
    ax3.axis('off')
    
    # Display blue channel
    ax4.imshow(blue_channel, cmap='gray')
    ax4.set_title('Blue Channel')
    ax4.axis('off')
    
    plt.tight_layout()
    plt.show()

# Specify the path to the image
image_path = "/home/ani/Desktop/test.png"

# Separate channels
red_channel, green_channel, blue_channel = separate_channels(image_path)

# Plot channels
plot_channels(red_channel, green_channel, blue_channel)
