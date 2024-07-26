import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def segment_image(image_array, threshold):
    # Convert image to grayscale if it's RGB
    if len(image_array.shape) == 3:
        # Convert RGB to grayscale using luminosity method
        image_array = np.dot(image_array[..., :3], [0.299, 0.587, 0.114])
    
    # Perform segmentation using thresholding
    segmented_image = np.where(image_array < threshold, 0, 255).astype(np.uint8)
    
    return segmented_image

def plot_segmented_image(image_path, threshold):
    # Load the image using matplotlib
    image_array = mpimg.imread(image_path)
    
    # Segment the image
    segmented_image = segment_image(image_array, threshold)
    
    # Display original and segmented images
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))
    
    # Display original image
    ax1.imshow(image_array, cmap='gray' if len(image_array.shape) == 2 else None)
    ax1.set_title('Original Image')
    ax1.axis('off')
    
    # Display segmented image
    ax2.imshow(segmented_image, cmap='gray')
    ax2.set_title(f'Segmented Image (Threshold: {threshold})')
    ax2.axis('off')
    
    plt.tight_layout()
    plt.show()

# Specify the path to the image and the threshold value
image_path = "/home/parrot/Desktop/test.png"
threshold_value = 120  # Adjust this threshold value as needed

# Plot segmented image
plot_segmented_image(image_path, threshold_value)
