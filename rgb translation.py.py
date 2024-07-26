import numpy as np
import matplotlib.pyplot as plt

# Image size and square size
image_size = 100
square_size = 20

# Create a 3-channel RGB image with np.zeros
image = np.zeros((image_size, image_size, 3), dtype=np.uint8)

# Set the blue channel (index 2) to 255 in the center square
start = (image_size - square_size) // 2
end = start + square_size
image[start:end, start:end, 2] = 255  # Blue channel set to 255 (full blue)

# Define translation parameters (shift in x and y directions)
shift_x = 30
shift_y = -20

# Create an empty array for the translated image
translated_image = np.zeros_like(image)

# Perform image translation manually
for x in range(image_size):
    for y in range(image_size):
        new_x = x + shift_x
        new_y = y + shift_y
        
        # Check if the new coordinates are within bounds
        if 0 <= new_x < image_size and 0 <= new_y < image_size:
            translated_image[new_x, new_y, :] = image[x, y, :]

# Visualize the original and translated images
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.title('Original Image')
plt.imshow(image)
plt.axis('off')

plt.subplot(1, 2, 2)
plt.title('Translated Image')
plt.imshow(translated_image)
plt.axis('off')

plt.tight_layout()
plt.show()
