import cv2
import numpy as np
import matplotlib.pyplot as plt

path = 'C:/Users/LENOVO/OneDrive/Pictures/Saved Pictures/duck-with-sunflower.jpg'
image = cv2.imread(path)
b, g, r = cv2.split(image)
image_2 = cv2.merge([r, g, b])
plt.subplot(121)