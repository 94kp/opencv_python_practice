import cv2
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("video_path", help="Path to video file")
args = parser.parse_args()

capture = cv2.VideoCapture(args.video_path)


if capture.isOpened() is False:
    print("Error: Camera could not be initialised")


frame_index = capture.get(cv2.CAP_PROP_FRAME_COUNT) - 1

while capture.isOpened() and frame_index >= 0:
    capture.set(cv2.CAP_PROP_POS_FRAMES, frame_index)

    ret, frame = capture.read()

    if ret:
        cv2.imshow('Frame', frame)
        frame_index -=1

        if cv2.waitKey(2) & 0xFF == ord('q'):
            break

capture.release()
cv2.destroyAllWindows()
