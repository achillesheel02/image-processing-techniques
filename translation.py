import numpy as np
import argparse
import imutils
import cv2

ap=argparse.ArgumentParser()
ap.add_argument('-i','--image',required=True,
                help="Path")
args=vars(ap.parse_args())

image=cv2.imread(args['image'])
cv2.imshow("Image",image)

M=np.float32([[1,0,25],[0,1,50]])
shifted=cv2.warpAffine(image,M,(image.shape[1],image.shape[0]))
cv2.imshow("Shifted",shifted)

M=np.float32([[1,0,-50],[0,1,-90]])
shifted[cv2.warpAffine(image,M,(image.shape[1],image.shape[0]))]
cv2.imshow("Shifted again",image)

shifted=imutils.translate(image,0,-100)
cv2.imshow('Down',shifted)
cv2.waitKey(0)