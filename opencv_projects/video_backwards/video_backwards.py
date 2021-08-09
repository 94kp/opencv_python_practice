import cv2
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("video_path", help = "path to video file")
args = parser.parse_args()

capture = cv2.VideoCapture(args.video_path)

if capture.isOpened() is False:
    print("Error opening video")

frame_index = capture.get(cv2.CAP_PROP_FRAME_COUNT) - 1

while capture.isOpened() and frame_index >= 0:

    capture.set(cv2.CAP_PROP_POS_FRAMES, frame_index)

    ret, frame = capture.read()

    if ret is True:
        cv2.imshow('Frame', frame)

        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        cv2.imshow('greyscale frame', gray_frame)

        frame_index -= 1

        print(f"next index to read: {frame_index}")

        if cv2.waitKey(2) & 0xFF == ord('q'):
            break
    else:
        break

capture.release()
cv2.destroyAllWindows()




