import cv2
import argparse

from hampy import HammingMarker

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--id', type=int)
    parser.add_argument('--size', type=int, default=64)
    args = parser.parse_args()

    m = HammingMarker(args.id) if args.id else HammingMarker.generate()
    img = (1 - m.toimage(args.size)) * 255

    cv2.imshow('marker_{}'.format(m.id), img)
    cv2.imwrite('marker_{}.png'.format(m.id), img)
    cv2.waitKey(-1)
