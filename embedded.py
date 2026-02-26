import cv2
import argparse

def embed_watermark(input_video, output_video):
    cap = cv2.VideoCapture(input_video)

    if not cap.isOpened():
        print("Error: Cannot open video file")
        return

    width = int(cap.get(3))
    height = int(cap.get(4))
    fps = cap.get(cv2.CAP_PROP_FPS)

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_video, fourcc, fps, (width, height))

    print("Embedding watermark...")

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Simple visible watermark for testing
        cv2.putText(frame, "USER_123", (50, 50),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1, (0, 0, 255), 2)

        out.write(frame)

    cap.release()
    out.release()
    print("Watermarked video saved as", output_video)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--output", default="watermarked_video.mp4")

    args = parser.parse_args()

    embed_watermark(args.input, args.output)