import cv2
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("path_to_image", help="Path to the image")

args = parser.parse_args()

image = cv2.imread(args.path_to_image)

cv2.imshow("original image", image)

cv2.waitKey(0)

smooth_image_gb = cv2.GaussianBlur(image, (9, 9), 0)

cv2.imshow("smooth image",smooth_image_gb)

cv2.waitKey(0)