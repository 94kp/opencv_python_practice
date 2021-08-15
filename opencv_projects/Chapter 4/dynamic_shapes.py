import cv2
import numpy as np
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



image = np.zeros((400, 400, 3), dtype="uint8")


image[:] = colors['light_gray']


################################# BE RIGHT BACK #######################################################

def draw_circle(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        print("event: EVENT_LBUTTONDBLCLK")
        cv2.circle(image, (x, y), 10, colors['magenta'], -1)
    
    if event == cv2.EVENT_MOUSEMOVE:
        print("event: EVETN_MOUSEMOVE")
    
    if event == cv2.EVENT_LBUTTONUP:
        print("event: EVENT_LBUTTONUP")

    if event == cv2.EVENT_LBUTTONDOWN:
        print("event: EVENT_LBUTTONDOWN")

cv2.namedWindow('Image Mouse')

cv2.setMouseCallback('Image Mouse', draw_circle)

show_with_matplotlib(image, 'dynamic shapes')