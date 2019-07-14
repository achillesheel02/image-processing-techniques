from matplotlib import pyplot as plt
import argparse

import cv2

ap=argparse.ArgumentParser()
ap.add_argument('-i','--image',required=True,
                help="Path")
args=vars(ap.parse_args())

image=cv2.imread(args['image'])
channels=cv2.split(image)
colors=('b','g','r')
plt.figure()
plt.title("Grayscale Hist")
for (channel,color) in zip(channels,colors):

    hist=cv2.calcHist([channel],[0],None,[256],[0,256])

    plt.plot(hist,color=color)
    plt.xlim([0, 256])



plt.show()
cv2.waitkey(0)