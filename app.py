import os
import time
from PIL import Image

# Set the directory path
directory = r""

# Set the interval to check for new files (in seconds)
interval = 10

while True:
    print(f"Checking for new PNG files in directory {directory}...")
    # Get a list of all PNG files in the directory and subdirectories
    png_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.png'):
                png_files.append(os.path.join(root, file))

    print(f"Found {len(png_files)} PNG files.")

    # Convert each PNG file to WebP and remove the original PNG file
    for file in png_files:
        print(f"Converting {file} to WebP...")
        img = Image.open(file)
        img.save(file.replace('.png', '.webp'), 'WEBP')
        os.remove(file)
        print(f"Removed {file}.")

    # Wait for the specified interval before checking again
    print(f"Waiting for {interval} seconds before checking again...")
    time.sleep(interval)

    # Check if any new files have been added to the directory
    new_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.png') and file not in png_files:
                new_files.append(os.path.join(root, file))
    if new_files:
        print(f"New PNG files detected: {new_files}")
        # Convert the new files to WebP and remove the original PNG file
        for file in new_files:
            print(f"Converting {file} to WebP...")
            img = Image.open(file)
            img.save(file.replace('.png', '.webp'), 'WEBP')
            os.remove(file)
            print(f"Removed {file}.")