import cv2
import numpy as np

# Load a color image first
path = 'C:/Users/LENOVO/OneDrive/Pictures/Saved Pictures/duck-with-sunflower.jpg'
image = cv2.imread(path)

# Access a pixel value by its row and column coordinates
pixel = image[100, 100]
print(pixel)

# Accessing only blue pixel
blue = image[100, 100, 0]
print(blue)

# Modifying the pixel values the same way
image[100, 100] = [255, 255, 255]
print(image[100, 100])

# Accessing RED Value
red = image.item(10, 10, 2)
print(red)

# Modifying RED Value
image.itemset((10, 10, 2), 100)
red = image.item(10, 10, 2)
print(red)
