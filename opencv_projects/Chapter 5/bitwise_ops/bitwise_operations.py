import cv2
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("image_path", help="path to image")
parser.add_argument("binary_image", help="path to binary image")

args = parser.parse_args()

img = cv2.imread(args.image_path)
binary_image = cv2.imread(args.binary_image)

cv2.imshow("original image", img)

cv2.waitKey(0)

bitwise_and = cv2.bitwise_and(img, binary_image)

bitwise_or = cv2.bitwise_or(img, binary_image)

cv2.imshow("Bitwise AND", bitwise_and)
cv2.waitKey(0)

cv2.imshow("Bitwise OR", bitwise_or)
cv2.waitKey(0)

## IMAGES NEED TO HAVE THE SAME SHAPE!!!!