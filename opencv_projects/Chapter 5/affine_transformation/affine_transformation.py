import cv2
import numpy as np
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("image_path", help = "Path to an image")

args = parser.parse_args()

image = cv2.imread(args.image_path)

height, width = image.shape[:2]

pts_1 = np.float32([[135, 45], [385, 45], [135, 230]])
pts_2 = np.float32([[135, 45], [385, 45], [150, 230]])

M = cv2.getAffineTransform(pts_1, pts_2)
dst_image = cv2.warpAffine(image, M, (width, height))

cv2.imshow("new image", dst_image)

cv2.waitKey(0)