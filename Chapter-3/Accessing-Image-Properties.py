import cv2

path = 'C:/Users/LENOVO/OneDrive/Pictures/Saved Pictures/duck-with-sunflower.jpg'
image = cv2.imread(path)
print(image.shape)
print(image.size)
print(image.dtype)
