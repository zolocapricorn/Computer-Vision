import cv2
import numpy as np
import random

# color
# red = random.randint(1, 255)
# green = random.randint(1, 255)
# blue = random.randint(1, 255)

# True if mouse is pressed
drawing = False

# If True, draw rectangle. Press 'm' to toggle to circle
mode = True


def draw_circle(event, x, y, flags, param):
    global ix, iy, drawing, mode, img2, img, red, green, blue

    # color but disco when mouse move
    # red = random.randint(1, 255)
    # green = random.randint(1, 255)
    # blue = random.randint(1, 255)

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y
        img2 = np.copy(img)
        # color but normal
        red = random.randint(1, 255)
        green = random.randint(1, 255)
        blue = random.randint(1, 255)

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            if mode == True:
                img = np.copy(img2)
                cv2.rectangle(img, (ix, iy), (x, y), (red, green, blue), 1) # ตามแนวแกน x
            else:
                cv2.circle(img, (x, y), 5, (red, green, blue), -1)

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        if mode == True:
            cv2.rectangle(img, (ix, iy), (x, y), (red, green, blue), 1)
        else:
            cv2.circle(img, (x, y), 5, (red, green, blue), -1)

img = np.zeros((512, 512, 3), np.uint8) #ภาพหลัก
img2 = np.zeros((512, 512, 3), np.uint8) #ภาพเก็บ
cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_circle)

while True:
    cv2.imshow('image', img)
    k = cv2.waitKey(1) & 0xFF
    if k == ord('m'):
        mode = False
    # Key ESC
    elif k == ord('s'):
        mode = True
    elif k == 27:
        break
cv2.destroyAllWindows()
