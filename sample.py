#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import argparse

import cv2 as cv
import numpy as np
from skimage.util import img_as_float
from skimage.filters import threshold_multiotsu


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("--device", type=int, default=0)
    parser.add_argument("--movie", type=str, default=None)

    args = parser.parse_args()

    # Initialize video capture
    cap_device = args.device
    if args.movie is not None:
        cap_device = args.movie
    cap = cv.VideoCapture(cap_device)

    while True:
        start_time = time.time()

        # Capture read
        ret, frame = cap.read()
        if not ret:
            break

        # Multi-Otsu Thresholding
        gray_image = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        sk_image = img_as_float(gray_image)

        thresholds = threshold_multiotsu(sk_image)
        regions = np.digitize(gray_image / 255.0, bins=thresholds)

        # Histogram
        histogram = cv.calcHist([gray_image], [0], None, [256], [0, 256])
        histogram = histogram / histogram.max()

        elapsed_time = time.time() - start_time

        # Draw Histogram
        height, width = 256, 256
        histogram_image = np.zeros((height, width, 3)) + 255

        for index, value in enumerate(histogram):
            if index == int(thresholds[0] * 255):
                cv.line(
                    histogram_image,
                    pt1=(index, 0),
                    pt2=(index, height),
                    color=(0, 255, 0),
                    thickness=1,
                    lineType=cv.LINE_4,
                )
            elif index == int(thresholds[1] * 255):
                cv.line(
                    histogram_image,
                    pt1=(index, 0),
                    pt2=(index, height),
                    color=(255, 0, 0),
                    thickness=1,
                    lineType=cv.LINE_4,
                )
            else:
                cv.line(
                    histogram_image,
                    pt1=(index, height),
                    pt2=(index, height - int(value * height)),
                    color=(0, 0, 0),
                    thickness=1,
                    lineType=cv.LINE_4,
                )

        # Draw regions
        apply_color_map_image = regions / regions.max() * 255
        apply_color_map_image = apply_color_map_image.astype(np.uint8)
        apply_color_map_image = cv.applyColorMap(
            apply_color_map_image,
            cv.COLORMAP_JET,
        )

        # Inference elapsed time
        cv.putText(
            frame,
            "Elapsed Time : " + '{:.1f}'.format(elapsed_time * 1000) + "ms",
            (10, 30), cv.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 1, cv.LINE_AA)

        key = cv.waitKey(1)
        if key == 27:  # ESC
            break
        cv.imshow('Input', frame)
        cv.imshow('Output', apply_color_map_image)
        cv.imshow('Histogram', histogram_image)

    cap.release()
    cv.destroyAllWindows()


if __name__ == '__main__':
    main()
