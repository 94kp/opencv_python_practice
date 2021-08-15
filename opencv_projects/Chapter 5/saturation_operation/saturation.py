import cv2
import numpy as np

x = np.uint8([250])
y = np.uint8([50])
# 250 + 50 = 300 => 255:
result_opencv = cv2.add(x, y)
print(f"cv2.add(x:'{x}', y: '{y}' = '{result_opencv}'")
# 250 + 50 = 300 % 256 = 44
result_numpy = x + y
print(f"x:'{x}' + y:'{y}' = '{result_numpy}'")