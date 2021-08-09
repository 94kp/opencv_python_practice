import cv2
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("image_path", help = "add path to image here")
parser.add_argument("image_output_path", help="specify image output folder here")

args = parser.parse_args()

img = cv2.imread(args.image_path)

print(args.image_path)
# cv2.imwrite(args["image_output_path"], img)

cv2.imshow("image", img)

cv2.imwrite(args.image_output_path, img)

cv2.waitKey(0)

