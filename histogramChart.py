import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

def calculate_histogram(image_array):
    # Initialize an array to store histogram values (bins range 0-255)
    histogram = np.zeros(256, dtype=int)

    # Iterate through each pixel value in the image array and count occurrences
    for pixel_value in image_array.flatten():
        histogram[pixel_value] += 1

    return histogram

def plot_image_and_histogram(image_path):
    # Read the image
    image = Image.open(image_path)

    # Convert image to grayscale if it's not already
    if image.mode != 'L':
        image = image.convert('L')

    # Convert image to numpy array
    image_array = np.array(image)

    # Display the image
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))
    ax1.imshow(image_array, cmap='gray')
    ax1.set_title('Image')
    ax1.axis('off')

    # Calculate the histogram
    hist_values = calculate_histogram(image_array)

    # Plot the histogram
    ax2.plot(hist_values, color='blue')
    ax2.set_title('Image Histogram')
    ax2.set_xlabel('Pixel Value')
    ax2.set_ylabel('Frequency')

    # Display plot
    plt.show()

# Specify the path to the image
image_path = "/home/ani/Desktop/test.png"

# Plot image and histogram
plot_image_and_histogram(image_path)
