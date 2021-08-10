import cv2
import argparse
import numpy as np
import matplotlib.pyplot as plt


#############

# Show with Matplotlib function


def show_with_matplotlib(img, title):
    img_RGB = img[:, :, ::-1]

    plt.imshow(img_RGB)
    plt.title(title)
    plt.show()


#############


colors = {'blue': (255, 0, 0), 'green': (0, 255, 0), 'red': (0, 0, 255), 'yellow': (0, 255, 255),
          'magenta': (255, 0, 255), 'cyan': (255, 255, 0), 'white': (255, 255, 255), 'black': (0, 0, 0),
          'gray': (125, 125, 125), 'rand': np.random.randint(0, high=256, size=(3,)).tolist(),
          'dark_gray': (50, 50, 50), 'light_gray': (220, 220, 220)}

image = np.zeros((400, 400, 3), dtype="uint8")

image[:] = colors['light_gray']

# show_with_matplotlib(image, 'Blank Canvas')

# cv2.line(image, (0,0), (400,400), colors['green'], 3)
# cv2.line(image, (0, 400), (400, 0), colors['blue'], 3)

# show_with_matplotlib(image, 'cv2.line()')

# cv2.rectangle(image, (10, 50), (60, 300), (colors['green']), 3)
# cv2.rectangle(image, (80, 50), (130, 300), colors['blue'], -1)

# show_with_matplotlib(image, 'cv2.rectangle()')

cv2.circle(image, (50,50), 20, colors['green'], 3)
cv2.circle(image, (100, 100), 30, colors['blue'], -1)

show_with_matplotlib(image, 'cv2.circle()')