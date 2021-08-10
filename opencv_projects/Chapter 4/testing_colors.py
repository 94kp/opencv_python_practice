import cv2
import numpy as np
import matplotlib.pyplot as plt
import constant


print(f"red: {constant.RED}")

def show_with_matplotlib(img, title):
    img_RGB = img[:, :, ::-1]

    plt.imshow(img_RGB)
    plt.title(title)
    plt.show()


colors = {'blue': (255, 0, 0), 'green': (0, 255, 0), 'red': (0, 0, 255), 'yellow': (0, 255, 255),
          'magenta': (255, 0, 255), 'cyan': (255, 255, 0), 'white': (255, 255, 255), 'black': (0, 0, 0),
          'gray': (125, 125, 125), 'rand': np.random.randint(0, high=256, size=(3,)).tolist(),
          'dark_gray': (50, 50, 50), 'light_gray': (220, 220, 220)}


image = np.zeros((500, 500, 3), dtype="uint8")

image[:] = colors['light_gray']

separation = 40

for key in colors:
    cv2.line(image, (0, separation), (500, separation), colors[key], 10)
    separation += 40

show_with_matplotlib(image, 'Dictionary with some predefined colors')