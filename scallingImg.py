import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import math

# Load the original PNG image using matplotlib
image_path = "/home/ani/Desktop/test.png"
original_image = mpimg.imread(image_path)

# Display the original image
plt.figure(figsize=(6, 6))
plt.title('Original Image')
plt.imshow(original_image)
plt.axis('off')
plt.show()

# Define scaling factors
scale_x = 1.5  # Scale factor in the x-direction
scale_y = 0.8  # Scale factor in the y-direction

# Determine the size of the original image
height, width, channels = original_image.shape

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
            scaled_image[x, y, :] = original_image[orig_x, orig_y, :]

# Display the scaled image
plt.figure(figsize=(6, 6))
plt.title('Scaled Image')
plt.imshow(scaled_image)
plt.axis('off')
plt.show()
