import cv2
import time
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("ip_url", help="ip address of camera", type=str)
args = parser.parse_args()

capture = cv2.VideoCapture(args.ip_url)

frame_width = capture.get(cv2.CAP_PROP_FRAME_WIDTH)
frame_height = capture.get(cv2.CAP_PROP_FRAME_HEIGHT)
fps = capture.get(cv2.CAP_PROP_FPS)

print("CV_CAP_PROP_FRAME_WIDTH: '{}'".format(frame_width))
print("CV_CAP_PROP_FRAME_HEIGHT: '{}'".format(frame_height))
print("CV_PROP_FPS: '{}'".format(fps))

if capture.isOpened() is False:
    print("Error opening the camera")

while capture.isOpened():
    ret, frame = capture.read()

    if ret is True:
        # cv2.imshow('Input frame from the camera', frame)
        processing_start = time.time()
        
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        processing_end = time.time()

        processing_time_frame = processing_end - processing_start

        print(f"fps: {1.0 / processing_time_frame}")

        cv2.imshow('Grayscale Input Camera', gray_frame)


        frame_index = 0
        if cv2.waitKey(20) & 0xFF == ord('c'):
            frame_name=f"camera_frame_{frame_index}.png"
            gray_frame_name = f"grayscale_camera_frame_{frame_index}.png"
            cv2.imwrite(frame_name, frame)
            cv2.imwrite(gray_frame_name, gray_frame)
            frame_index += 1

        if cv2.waitKey(20) & 0xFF == ord('q'):
            break
    else:
        break

capture.release()
cv2.destroyAllWindows()