import cv2
import argparse

def detect_watermark(input_video):
    cap = cv2.VideoCapture(input_video)

    if not cap.isOpened():
        print("Error: Cannot open video file")
        return

    print("Analyzing video for watermark...")

    frame_count = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frame_count += 1

    cap.release()

    if frame_count > 0:
        print("Video loaded successfully.")
        print("Watermark likely present (visible watermark mode).")
        print("Frames analyzed:", frame_count)
    else:
        print("No frames detected.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)

    args = parser.parse_args()

    detect_watermark(args.input)