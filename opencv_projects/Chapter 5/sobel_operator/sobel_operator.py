import cv2
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("image_path", help="path to image")

args = parser.parse_args()

img = cv2.imread(args.image_path)

cv2.imshow("original image", img)

cv2.waitKey(0)

gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

gradient_x = cv2.Sobel (gray_image, cv2.CV_16S, 1, 0, 3)
gradient_y = cv2.Sobel(gray_image, cv2.CV_16S, 0, 1, 3)

abs_gradient_x = cv2.convertScaleAbs(gradient_x)
abs_gradient_y = cv2.convertScaleAbs(gradient_y)

sobel_image = cv2.addWeighted(abs_gradient_x, 0.5, abs_gradient_y, 0.5, 0)

cv2.imshow("original image", img)
cv2.imshow("gradient_x", gradient_x)
cv2.imshow("gradient_y", gradient_y)
cv2.imshow("sobel_image", sobel_image)

cv2.waitKey(0)