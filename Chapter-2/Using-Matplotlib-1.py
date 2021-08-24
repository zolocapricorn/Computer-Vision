import numpy as np
import cv2
import matplotlib.pyplot as plt

path = 'C:/Users/LENOVO/OneDrive/Pictures/Saved Pictures/duck-with-sunflower.jpg'
image = cv2.imread(path, 0)
plt.imshow(image, cmap='gray', interpolation='bicubic')

# เพื่อซ่อนขีดบนแกน x และแกน y
plt.xticks([]), plt.yticks([])
plt.show()
