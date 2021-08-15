import cv2
import numpy as np
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("image_path", help = "Path to an image")

args = parser.parse_args()

image = cv2.imread(args.image_path)

(b, g, r) = cv2.split(image)

cv2.imshow("blue", b)
cv2.imshow("green", g)
cv2.imshow("red", r)

cv2.waitKey(0)