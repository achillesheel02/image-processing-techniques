import numpy as np
import argparse
import cv2

qp=argparse.ArgumentParser()
qp.add_argument('-i','--image',required=True,help="Path")
args=vars(qp.parse_args())

image=cv2.imread(args['image'])
image=cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)
blurred=cv2.GaussianBlur(image,(5,5),0)
cv2.imshow("Image",image)

(T, thresh)=cv2.threshold(blurred,120,255,cv2.THRESH_BINARY)
cv2.imshow("Thresh Bin",thresh)
(T, threshinv)=cv2.threshold(blurred,120,255,cv2.THRESH_BINARY_INV)
cv2.imshow("Thresh BinInv",threshinv)
cv2.imshow("djd",cv2.bitwise_and(image,image,mask=threshinv))
cv2.waitKey(0)