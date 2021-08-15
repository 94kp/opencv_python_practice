import cv2
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("image_path", help="path to image")

args = parser.parse_args()

img = cv2.imread(args.image_path)

cv2.imshow("original image", img)

cv2.waitKey(0)

r_img = cv2.resize(img, None,fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)

cv2.imshow("resized image", r_img)

cv2.waitKey(0)