import numpy as np
import cv2

cap = cv2.VideoCapture("C:/Users/LENOVO/Videos/Captures/Neo4j Installation.mp4")

while (cap.isOpened()):
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('frame', gray)
    if cv2.waitKey(25) & 0xFF == ord("g"):
        break

cap.release()
