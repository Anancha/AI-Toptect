# Anucha Ananbenjapon Edit
import cv2
print(cv2.__version__)
import numpy as np
while True:
    frame = np.zeros([250,250],dtype=np.uint8)
    frame[:,0:125] = 255
    cv2.imshow('My Windows',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
