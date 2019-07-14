import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True,
                help = "Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(image, (3,3), 0)
cv2.imshow("Image", image)
canny=cv2.Canny(image,130,190)
cv2.imshow('canny',canny)

(_, cnts, _) = cv2.findContours(canny.copy(), cv2.RETR_EXTERNAL,
       cv2.CHAIN_APPROX_SIMPLE)
hand=image.copy()
cv2.drawContours(hand,cnts,-1,(0,0,0),2)
cv2.imshow('hand',hand)

for (i, c) in enumerate(cnts):
    (x, y, w, h) = cv2.boundingRect(c)

    print("Coin #{}".format(i + 1))
    coin = image[y:y + h, x:x + w]
    cv2.imshow("Coin", coin)
    mask = np.zeros(image.shape[:2], dtype = "uint8")

    mask = mask[y:y + h, x:x + w]
    cv2.imshow("Masked Coin", cv2.bitwise_and(coin, coin, mask = mask))
    cv2.waitKey(0)
print(hand)