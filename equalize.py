from matplotlib import pyplot as plt
import argparse
import numpy as np
import cv2

ap=argparse.ArgumentParser()
ap.add_argument('-i','--image',required=True,
                help="Path")
args=vars(ap.parse_args())

image=cv2.imread(args['image'])
image=cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)

eq=cv2.equalizeHist(image)
cv2.imshow("Eq",np.hstack([image,eq]))
cv2.waitKey(0)