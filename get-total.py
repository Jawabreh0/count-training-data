import os
import glob

# Set the directory path where your images are stored
directory_path = "/home/jawabreh/Desktop/Face-Mask-Detection-master/dataset/with_mask"

# Use the glob module to get a list of all image files in the directory
image_files = glob.glob(os.path.join(directory_path, "*.jpg")) + \
              glob.glob(os.path.join(directory_path, "*.jpeg")) + \
              glob.glob(os.path.join(directory_path, "*.png"))

# Print the total number of images found
print(f"Total number of images found: {len(image_files)}")
