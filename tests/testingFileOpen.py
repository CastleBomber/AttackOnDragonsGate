#!/usr/bin/env python
import re

def main():
    d = dict()
    d = {"0": [0x0, 111, 0x0],
         "1": [255, 0x0, 255],
         "2": [0x0, 0x0, 255],
         "3": [0x0, 255, 255],
         "4": [0x0, 255, 0x0],
         "5": [255, 255, 0x0],
         "6": [255,0xBE, 0x0],
         "7": [255, 0x0, 0x0],
         "9": [255, 255, 255]}

    fo = open("pixels", "r")
    pixelStr = fo.read()
    pixelStr = re.sub(r"[\n\t\s]*", "", pixelStr)

    firstPixel = pixelStr[0]    

    print(firstPixel)
    print(d[firstPixel][1])

    fo.close()


main()
