import cv2
import argparse
import numpy as np
from matplotlib import pyplot as plt

def show_img_with_matplotlib(color_img, title, pos):
    img_RGB = color_img[:, :, ::-1]

    ax = plt.subplot(2, 3, pos)
    plt.imshow(img_RGB)
    plt.title(title)
    plt.axis('off')


def color_quantization(image, k):
    data = np.float32(image).reshape((-1, 3))
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 20, 1.0)

    ret, label, center = cv2.kmeans(data, k, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)

    center = np.uint8(center)
    result = center[label.flatten()]
    result = result.reshape(image.shape)
    return result

parser = argparse.ArgumentParser()

parser.add_argument("image_path", help="Path to my image")

args = parser.parse_args()

image = cv2.imread(args.image_path)

## First transform the image into data

# data = np.float32(image).reshape((-1, 3))

## If we want only 3 colors---

## load the BGR image
## we already loaded it

color_1 = color_quantization(image, 1)
color_2 = color_quantization(image, 2)
color_3 = color_quantization(image, 3)
color_4 = color_quantization(image, 4)
color_5 = color_quantization(image, 5)
color_6 = color_quantization(image, 20)
# color_3 = color_quantization(image, 3)

# cv2.imshow("color quantised",color_3)

# show_img_with_matplotlib(color_3, "image with color_quantisation 3", 0)
# show_img_with_matplotlib(image, "original image", 0)

cv2.imshow("Original Image",image)
cv2.waitKey(0)

show_img_with_matplotlib(color_1, "image with color_quantisation 1", 1)
show_img_with_matplotlib(color_2, "image with color_quantisation 2", 2)
show_img_with_matplotlib(color_3, "image with color_quantisation 3", 3)
show_img_with_matplotlib(color_4, "image with color_quantisation 4", 4)
show_img_with_matplotlib(color_5, "image with color_quantisation 5", 5)
show_img_with_matplotlib(color_6, "image with color_quantisation 20", 6)

plt.show()