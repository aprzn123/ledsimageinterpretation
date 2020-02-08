import cv2
import numpy as np
import matplotlib.pyplot as plt
import argparse


def toHex(arr):
    return arr[0] * 0x000001 + arr[1] * 0x000100 + arr[2] * 0x010000

imArray = cv2.imread('laser.png')
color_data = "{"
frames = "{"
for frame in range(0, len(imArray), 8):
    colors = set()
    # actual frame open
    color_data += "{"
    frames += "{"
    for col in range(0, len(imArray[frame])):
        for row in range(frame, frame + 8):
            hex_val = toHex(imArray[row][col])
            if hex_val != 0:
                colors.add(hex_val)
    for color in colors:
        # color data open
        frames += "{"
        color_data += hex(color) + ", "
        for col in range(0, len(imArray[frame])):
            for row in range(frame, frame + 8):
                num_represent = 0
                hex_color = toHex(imArray[row][col])
                num_represent += (1 if hex_color == color else 0) * (2 ** (row - frame))
                frames += hex(num_represent)
                frames += ", "
        frames = frames[0:-2]
        frames += "}, "
    color_data = color_data[0:-2]
    frames = frames[0:-2]
    frames += "}, "
    color_data += "}, "
color_data = color_data[0:-2]
frames = frames[0: -2]
color_data += "}"
frames += "}"
print(frames)
