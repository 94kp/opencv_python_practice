import cv2
import argparse
import numpy as np

parser = argparse.ArgumentParser()

parser.add_argument("image_path", help="path to the image")

args = parser.parse_args()

image = cv2.imread(args.image_path)

height, width = image.shape[:2]
M = cv2.getRotationMatrix2D((width / 2.0, height / 2.0), 180, 1)
dst_image = cv2.warpAffine(image, M,(width, height))

cv2.imshow("rotated",dst_image)

cv2.waitKey(0)