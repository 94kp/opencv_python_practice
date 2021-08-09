import cv2
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("camera_index", help="Index of the camera", type=int)
args = parser.parse_args()

capture = cv2.VideoCapture(args.camera_index)

if capture.isOpened() is False:
    print("Error starting the camera")

while capture.isOpened():
    ret, frame = capture.read()

    if ret:
        cv2.imshow("frame",frame)

        if cv2.waitKey(2) & 0xFF == ord('q'):
            break
    else:
        break

capture.release()
cv2.destroyAllWindows()