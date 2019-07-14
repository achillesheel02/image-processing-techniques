import numpy as np
import argparse
import imutils
import cv2

ap=argparse.ArgumentParser()
ap.add_argument('-i','--image',required=True,
                help="Path")
args=vars(ap.parse_args())

image=cv2.imread(args['image'])
cv2.imshow("Oriji",image)

(h,w)=image[:2]
h=h//2
w=w//2
start=h-30
end=w-40
cropped=image[50:100,50:100]
cv2.imshow("Centre crop",cropped)
cv2.waitKey(0)