import cv2
import argparse

from arpy import detect_markers

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--camera', type=int, default=-1)
    args = parser.parse_args()

    cap = cv2.VideoCapture(args.camera)

    while True:
        okay, img = cap.read()
        if not okay:
            continue

        markers = detect_markers(img)

        for m in markers:
            m.draw_contour(img)

        cv2.imshow('live', img)
        cv2.waitKey(20)
