import cv2
import numpy as np
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("image_path", help = "Path to an image")

args = parser.parse_args()

image = cv2.imread(args.image_path)

cv2.imshow("original image", image)
cv2.waitKey(0)

smoothed = cv2.GaussianBlur(image, (9, 9), 10)
unsharped = cv2.addWeighted(image, 1.5, smoothed, -0.5, 0)

cv2.imshow("unsharp masking",unsharped)
cv2.waitKey(0)