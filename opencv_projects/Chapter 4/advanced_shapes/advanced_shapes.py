import cv2
import numpy as np
import argparse
import matplotlib.pyplot as plt


#######################################

# Show with Matplotlib function


def show_with_matplotlib(img, title):
    img_RGB = img[:, :, ::-1]

    plt.imshow(img_RGB)
    plt.title(title)
    plt.show()


#######################################


colors = {'blue': (255, 0, 0), 'green': (0, 255, 0), 'red': (0, 0, 255), 'yellow': (0, 255, 255),
          'magenta': (255, 0, 255), 'cyan': (255, 255, 0), 'white': (255, 255, 255), 'black': (0, 0, 0),
          'gray': (125, 125, 125), 'rand': np.random.randint(0, high=256, size=(3,)).tolist(),
          'dark_gray': (50, 50, 50), 'light_gray': (220, 220, 220)}



image = np.zeros((300, 300, 3), dtype="uint8")

image[:] = colors['light_gray']

# cv2.line(image, (0,0), (300, 300), colors['green'], 3)
# cv2.rectangle(image, (0, 0), (100, 100), colors['blue'], 3)
# ret, p1, p2 = cv2.clipLine((0, 0, 100, 100), (0, 0), (300, 300))
# if ret:
#     cv2.line(image, p1, p2, colors['yellow'], 3)

# show_with_matplotlib(image, 'clipLine')

# cv2.arrowedLine(image, (50, 50), (200, 50), colors['red'], 3, 8, 0, 0.1)
# cv2.arrowedLine(image, (50, 120), (200, 120), colors['green'], 3, cv2.LINE_AA, 0, 0.3)

# show_with_matplotlib(image, 'arrowedLine')

# cv2.ellipse(image, (80, 80), (60, 40), 0, 0, 360, colors['red'], -1)
# show_with_matplotlib(image, 'ellipse')

# pts = np.array([[250, 5], [220, 80], [280, 80]], np.int32)
# pts = pts.reshape((-1, 1, 2))
# print(f"shape of pts {pts.shape}")
# cv2.polylines(image, [pts], True, colors['green'], 3)

shift=3
factor=2 ** shift
print(f"factor: {factor}")
cv2.circle(image, (int(round(299.9 * factor)), int(round(299.99 * factor))), 300, colors['green'], 1)