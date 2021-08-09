import cv2
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("camera_index", help = "Enter camera number", type = int)
args = parser.parse_args()

capture = cv2.VideoCapture(args.camera_index)

frame_width = capture.get(cv2.CAP_PROP_FRAME_WIDTH)
print(f"CAP_PROP_FRAME_WIDTH: {frame_width}")

if capture.isOpened() is False:
    print("Error camera could not be started")

while capture.isOpened():
    ret, frame = capture.read()

    if ret:
        cv2.imshow("frame", frame)

        if cv2.waitKey(2) & 0xFF == ord('q'):
            break
    else:
        break

capture.release()
cv2.destroyAllWindows()