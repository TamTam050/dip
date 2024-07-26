import numpy as np
import matplotlib.pyplot as plt
import math

# Create a 3-channel RGB image manually
image_size = 100
image = np.zeros((image_size, image_size, 3), dtype=np.uint8)

# Draw a red circle in the center
center_x, center_y = image_size // 2, image_size // 2
radius = 20
for x in range(image_size):
    for y in range(image_size):
        if math.sqrt((x - center_x)**2 + (y - center_y)**2) <= radius:
            image[x, y, 0] = 255  # Red channel set to 255 (full red)

# Display the original image
plt.figure(figsize=(6, 6))
plt.title('Original Image')
plt.imshow(image)
plt.axis('off')
plt.show()

# Define scaling factors
scale_x = 0.7  # Scale factor in the x-direction
scale_y = 1.5  # Scale factor in the y-direction

# Determine the size of the original image
height, width, channels = image.shape

# Calculate new dimensions after scaling
new_height = int(height * scale_y)
new_width = int(width * scale_x)

# Initialize an array for the scaled image
scaled_image = np.zeros((new_height, new_width, channels), dtype=np.uint8)

# Perform image scaling manually
for x in range(new_height):
    for y in range(new_width):
        # Calculate corresponding coordinates in the original image
        orig_x = int(x / scale_y)
        orig_y = int(y / scale_x)
        
        # Copy pixel value to scaled image if within original bounds
        if 0 <= orig_x < height and 0 <= orig_y < width:
            scaled_image[x, y, :] = image[orig_x, orig_y, :]

# Display the scaled image
plt.figure(figsize=(6, 6))
plt.title('Scaled Image')
plt.imshow(scaled_image)
plt.axis('off')
plt.show()
