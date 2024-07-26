import numpy as np
import matplotlib.pyplot as plt

def bit_plane_slice(image_array, bit_position):
    # Perform bit-plane slicing
    bit_plane = (image_array >> bit_position) & 1
    return bit_plane

def plot_bit_plane_slices(image_path):
    # Read the image
    image_array = plt.imread(image_path)
    
    # Convert image to grayscale if it's not already
    if len(image_array.shape) == 3:
        # Assuming the image is RGB, convert to grayscale
        image_array = np.dot(image_array[..., :3], [0.299, 0.587, 0.114])
    
    # Convert to 8-bit image (0-255 range) if necessary
    if image_array.max() > 1:
        image_array = (image_array / image_array.max() * 255).astype(np.uint8)
    else:
        image_array = (image_array * 255).astype(np.uint8)
    
    # Create subplots for bit plane slices
    fig, axs = plt.subplots(2, 4, figsize=(12, 6))
    axs = axs.ravel()
    
    # Display original image
    axs[0].imshow(image_array, cmap='gray')
    axs[0].set_title('Original Image')
    axs[0].axis('off')
    
    # Perform bit-plane slicing for each bit position
    for i in range(1, 9):
        bit_plane = bit_plane_slice(image_array, i-1)
        axs[i].imshow(bit_plane, cmap='gray')
        axs[i].set_title(f'Bit Plane {i-1}')
        axs[i].axis('off')
    
    plt.tight_layout()
    plt.show()

# Specify the path to the image
image_path = "/home/parrot/Desktop/test.png"

# Plot bit plane slices
plot_bit_plane_slices(image_path)
