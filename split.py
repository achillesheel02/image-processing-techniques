import numpy as np
import argparse
import imutils
import cv2

ap=argparse.ArgumentParser()
ap.add_argument('-i','--image',required=True,
                help="Path")
args=vars(ap.parse_args())

image=cv2.imread(args['image'])
(b,g,r)=cv2.split(image)

cv2.imshow("Red",r)
cv2.imshow("Green",g)
cv2.imshow("Blue",b)

merged=cv2.merge([b,g,r])
cv2.imshow('Merged',merged)
cv2.waitKey(0)
