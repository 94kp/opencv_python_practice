import cv2
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("first_number", help="enter the first number here", type=int)
args = parser.parse_args()

print(args.first_number)