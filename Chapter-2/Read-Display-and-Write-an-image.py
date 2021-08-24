import cv2


path = 'C:/Users/LENOVO/OneDrive/Pictures/Saved Pictures/duck-with-sunflower.jpg'
image = cv2.imread(path)
cv2.imshow('', image)
kkk = cv2.waitKey(0)
if kkk == 27:
    cv2.destroyAllWindows()
elif kkk == ord('s'):
    cv2.imwrite('test01gray.png', image)
    cv2.destroyAllWindows()
