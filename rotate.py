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


(h,w)=image.shape[:2]
centre=(w//2,h//2)

M= cv2.getRotationMatrix2D(centre,45,1.0)
rotated=cv2.warpAffine(image,M,(w,h))
cv2.imshow("45", rotated)

M=cv2.getRotationMatrix2D(centre,-90,1.0)
rotated=cv2.warpAffine(image,M,(w,h))
cv2.imshow("-90",rotated)

image=imutils.rotate(image,centre,200,2,w,h)
cv2.imshow("270",image)
cv2.waitKey(0)