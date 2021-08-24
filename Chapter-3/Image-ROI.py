import cv2

path = 'C:/Users/LENOVO/OneDrive/Pictures/Saved Pictures/duck-with-sunflower.jpg'
image = cv2.imread(path)
duck = image[5:115, 115:120]
image_copy = image.copy()
image