import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True,
                help = "Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Image", image)
lap=cv2.Laplacian(image,cv2.CV_64F)
lap=np.uint8(np.absolute(lap))
cv2.imshow("Laplacian",lap)

sobelx=cv2.Sobel(image,cv2.CV_64F,1,0)
sobely=cv2.Sobel(image,cv2.CV_64F,0,1)
sobelx=np.uint8(np.absolute(sobelx))
sobely=np.uint8(np.absolute(sobely))

sobelc=cv2.bitwise_or(sobelx,sobely)
cv2.imshow('x',sobelx)
cv2.imshow('y',sobely)
cv2.imshow('c',sobelc)
cv2.waitKey(0)
