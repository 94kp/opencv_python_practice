import cv2
import argparse
import numpy as np

parser = argparse.ArgumentParser()

parser.add_argument("image_path", help="path to the image")

args = parser.parse_args()

image = cv2.imread(args.image_path)

height, width = image.shape[:2]

M = np.float32([[1, 0, 200],[0, 1, 30]])
dst_image = cv2.warpAffine(image, M, (width, height))

cv2.imshow("new image", dst_image)
cv2.waitKey(0)