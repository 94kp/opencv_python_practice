import cv2
import sys
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("first_number", help="first argument to be added", type=int)
parser.add_argument("second_number", help="second argument to be added", type=int)

args = parser.parse_args()

print("args: '{}'".format(args.first_number + args.second_number))
args_dict = vars(parser.parse_args())

print("args_dict dictionary: '{}'".format(args_dict))

print("first argument from the dictionary: '{}'".format(args_dict["first_number"]))
# print("Name of the program: {}".format(sys.argv[0]))
# print("number of arguments: {}".format(len(sys.argv)))
# print("Arguments: {}".format(str(sys.argv)))

path = "images/logo.png"
img = cv2.imread(path)

dimensions = img.shape

total_number_of_elements = img.size

image_dtype = img.dtype

cv2.imshow("original image", img)

cv2.waitKey(0)

(b, g, r) = img[6, 40]

gray_img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)

cv2.imshow("greyscaled image", gray_img)

cv2.waitKey(0)

i = gray_img[6, 40]