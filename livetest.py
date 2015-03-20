import cv2
import argparse

from hampy import detect_markers

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

            cv2.putText(img, str(m.id), tuple(int(p) for p in m.center),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 3)

        cv2.imshow('live', img)
        cv2.waitKey(20)
