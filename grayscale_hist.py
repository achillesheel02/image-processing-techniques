from matplotlib import pyplot as plt
import argparse

import cv2

ap=argparse.ArgumentParser()
ap.add_argument('-i','--image',required=True,
                help="Path")
args=vars(ap.parse_args())

image=cv2.imread(args['image'])
image=cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)
cv2.imshow("Grayscale",image)
hist=cv2.calcHist([image],[0],None,[256],[0,256])

plt.figure()
plt.title("Grayscale Hist")
plt.plot(hist)
plt.xlim([0,256])
plt.show()
cv2.waitkey(0)