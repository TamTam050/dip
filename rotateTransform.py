# Image Transformation Script - Without skimage

# 1. Importing Libraries
import numpy as np               # Library for numerical operations
import matplotlib.pyplot as plt  # Library for plotting
import math                      # Library for mathematical functions
from PIL import Image            # Python Imaging Library for image manipulation

# 2. Loading the Original Image
image_path = "/home/ani/Desktop/test.png"
original_image = Image.open(image_path)

# Convert image to numpy array
original_array = np.array(original_image)

# 3. Transformation Matrix and Applying Transformation
# Transformation matrix for rotation by 30 degrees
theta = math.radians(30)        # Convert angle to radians
cos_theta = math.cos(theta)     # Compute cosine of angle
sin_theta = math.sin(theta)     # Compute sine of angle

# Define transformation matrix for 2D rotation
t = np.array([[cos_theta, -sin_theta, 0],
              [sin_theta, cos_theta, 0],
              [0, 0, 1]])

# Getting the size of the image
height, width, channels = original_array.shape

# Calculate new image size after rotation
new_height = int(abs(width * sin_theta) + abs(height * cos_theta))
new_width = int(abs(height * sin_theta) + abs(width * cos_theta))

# Initializing a transformed image array
transformed_image = np.zeros((new_height, new_width, channels), dtype=np.uint8)

# Applying the transformation to each pixel in the image
for x in range(height):
    for y in range(width):
        # Calculate new coordinates after rotation using transformation matrix
        new_x = int(x * cos_theta - y * sin_theta)
        new_y = int(x * sin_theta + y * cos_theta)

        # Ensure new coordinates are within bounds
        if 0 <= new_x < new_height and 0 <= new_y < new_width:
            transformed_image[new_x, new_y, :] = original_array[x, y, :]

# Convert transformed image back to PIL Image
transformed_image_pil = Image.fromarray(transformed_image)

# 4. Visualizing Original and Transformed Images
# Visualizing the original and transformed images using matplotlib
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.title('Original Image')
plt.imshow(original_array)
plt.axis('off')

plt.subplot(1, 2, 2)
plt.title('Transformed Image')
plt.imshow(transformed_image_pil)
plt.axis('off')

plt.tight_layout()
plt.show()
