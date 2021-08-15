import cv2
import argparse
import numpy as np

parser = argparse.ArgumentParser()

parser.add_argument("image_path", help="path to the image")

args = parser.parse_args()

image = cv2.imread(args.image_path)

height, width = image.shape[:2]

cv2.imshow("original image", image)
cv2.waitKey(0)

def rotate(event, height, width, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:

        M = cv2.getRotationMatrix2D((width, height), 30, 1)
        dst_image = cv2.warpAffine(image, M, (width, height))

        cv2.imshow("new image", dst_image)
        cv2.waitKey(0)



cv2.namedWindow('Image Mouse')

cv2.setMouseCallback('Image Mouse', rotate)

cv2.waitKey(0)
