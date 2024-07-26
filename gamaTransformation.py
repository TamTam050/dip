import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

def gamma_correction(image_path, gamma):
    # Read the image
    image = Image.open(image_path)
    
    # Convert image to numpy array
    image_array = np.array(image)
    
    # Normalize pixel values to range [0, 1]
    image_array = image_array / 255.0
    
    # Apply gamma transformation
    gamma_corrected = np.power(image_array, gamma)
    
    # Scale values back to range [0, 255] and convert to uint8
    gamma_corrected = (gamma_corrected * 255).astype(np.uint8)
    
    return gamma_corrected

def plot_gamma_transformed_image(image_path, gamma):
    # Perform gamma correction
    gamma_corrected = gamma_correction(image_path, gamma)
    
    # Display original and gamma corrected images
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))
    
    # Display original image
    original_image = Image.open(image_path)
    ax1.imshow(original_image)
    ax1.set_title('Original Image')
    ax1.axis('off')
    
    # Display gamma corrected image
    ax2.imshow(gamma_corrected)
    ax2.set_title(f'Gamma Corrected (Gamma: {gamma})')
    ax2.axis('off')
    
    plt.tight_layout()
    plt.show()

# Specify the path to the image and the gamma value
image_path = "/home/ani/Desktop/img.png"
gamma_value = 1.5  # Adjust this gamma value as needed

# Plot gamma transformed image
plot_gamma_transformed_image(image_path, gamma_value)
