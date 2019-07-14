import numpy as np
import cv2

canvas=np.zeros((300,300,3),dtype='uint8')
cv2.rectangle(canvas,(5,5),(200,225),(30,30,30),2)
cv2.imshow("Canvas",canvas)
cv2.waitKey(0)