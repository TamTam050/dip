import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def translate_image(image_array, shift_x, shift_y):
    # Determine the size of the original image
    height, width, channels = image_array.shape
    
    # Create an empty array for the translated image
    translated_image = np.zeros_like(image_array)
    
    # Perform image translation
    for x in range(height):
        for y in range(width):
            new_x = x + shift_x
            new_y = y + shift_y
            
            # Check if the new coordinates are within bounds of the translated image
            if 0 <= new_x < height and 0 <= new_y < width:
                translated_image[new_x, new_y, :] = image_array[x, y, :]
    
    return translated_image

def plot_translated_image(image_path, shift_x, shift_y):
    # Load the image using matplotlib
    image_array = mpimg.imread(image_path)
    
    # Perform translation
    translated_image = translate_image(image_array, shift_x, shift_y)
    
    # Display original and translated images
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))
    
    # Display original image
    ax1.imshow(image_array)
    ax1.set_title('Original Image')
    ax1.axis('off')
    
    # Display translated image
    ax2.imshow(translated_image)
    ax2.set_title('Translated Image')
    ax2.axis('off')
    
    plt.tight_layout()
    plt.show()

# Specify the path to the image and translation parameters
image_path = "/home/parrot/Desktop/test.png"
shift_x = 50  # Translation in x direction
shift_y = 30  # Translation in y direction

# Plot translated image
plot_translated_image(image_path, shift_x, shift_y)
