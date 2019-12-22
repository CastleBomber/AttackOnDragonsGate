#!/usr/bin/env python
'''
sudo ./driver.py --led-rows=32 --led-cols=32  --led-brightness=40 --led-pwm-lsb-nanoseconds=300 --led-slowdown-gpio=2
'''
from samplebase import SampleBase
import pyaudio
import re
import os
import time


d = dict()
d = {"0": [0x0, 0x0, 0x0], # Black
     "1": [255, 0x0, 255], # Purple
     "2": [0x0, 0x0, 255], # Dark Blue
     "3": [0x0, 255, 255], # Light Blue
     "4": [0x0, 255, 0x0], # Green
     "5": [255, 255, 0x0], # Yellow
     "6": [255, 103, 0x0], # Blaze Orange
     "7": [255, 0x0, 0x0], # Red
     "8": [ 75,  25, 0x0], # Brown
     "9": [255, 255, 255], # White
     "A": [0xFF, 0x0, 0xFF], # Color of Thoughts
     "B": [0x8F, 0x0, 0XFF],  # Dragon's Eyes || M's
     "C": [0xA5, 0x2A, 0x2A], # Aubrun
     "E": [ 0xDB, 0xE9, 0xF4], # Dragon's Claws
     "D": [0xD8, 0x91, 0xEF], # Bright Lilac
     "R": [0x80, 0x00, 0x20]
     }


songBPM = 90
microBPM = (60000/songBPM)*(1000) # ms, used for usleep

'''
    CastleBomber sigil/ show
'''
class LightShow(SampleBase):

    
    def __init__(self, *args, **kwargs):
        super(LightShow, self).__init__(*args, **kwargs)
    
    # all the work is done here
    # self.functionCall(arguments)
    def run(self):
        self.sceneFlipThroughCount("whiteMoonScene", 1)
        self.goRight("bomb_right_wb")
        self.sceneFlipThroughCount("finalScene", 1)
        self.usleep(999999999)

    # @param sheet - pixelSheet to show off
    def showMyWork(self, sheet):
        canvas = self.matrix.CreateFrameCanvas()
        sheetName = sheet
        
        fo = open('/home/pi/Desktop/pixelSheets/' + sheetName)
        pixelStr = fo.read()
        pixelStr = re.sub(r"[\n\t\s]*", "", pixelStr)
        count = 0

        for y in range(0, 32):
            for x in range(0, 32):
                pixelPos = pixelStr[x+(y*32)]
                canvas.SetPixel( x, y,
                                 d[pixelPos][0],
                                 d[pixelPos][1],
                                 d[pixelPos][2])
        canvas = self.matrix.SwapOnVSync(canvas)
        self.usleep(999999999)
        fo.close()

    # show off work located in a far off directory
    # @param sheet - pixelSheet to show off
    def showMyWorkInDir(self, sheet):
        canvas = self.matrix.CreateFrameCanvas()
        sheetName = sheet
        
        fo = open('/home/pi/Desktop/' + sheetName)
        pixelStr = fo.read()
        pixelStr = re.sub(r"[\n\t\s]*", "", pixelStr)
        count = 0

        for y in range(0, 32):
            for x in range(0, 32):
                pixelPos = pixelStr[x+(y*32)]
                canvas.SetPixel( x, y,
                                 d[pixelPos][0],
                                 d[pixelPos][1],
                                 d[pixelPos][2])
        canvas = self.matrix.SwapOnVSync(canvas)
        self.usleep(microBPM)
        fo.close()

    # randomly goes through all sheets
    def rndmFlipThrough(self):
        canvas = self.matrix.CreateFrameCanvas()
        while True:
            for file in os.listdir('/home/pi/Desktop/pixelSheets'):
                fo = open(os.path.join('/home/pi/Desktop/pixelSheets', file))
                pixelStr = fo.read()
                pixelStr = re.sub(r"[\n\t\s]*", "", pixelStr)

                print("filename: " + file)

                for y in range(0, 32):
                    for x in range(0, 32):
                        pixelPos = pixelStr[x+(y*32)]
                        canvas.SetPixel( x, y,
                                        d[pixelPos][0],
                                        d[pixelPos][1],
                                        d[pixelPos][2])
                canvas = self.matrix.SwapOnVSync(canvas)
                self.usleep(999999)
                fo.close()

    
    # Sigil goes left,
    # set up count for 32 steps
    # would slowly slide up if not stopped
    def goLeft(self, sheet):
        canvas = self.matrix.CreateFrameCanvas()
        sheetName = sheet
        fo = open('/home/pi/Desktop/pixelSheets/' + sheetName)
        pixelStr = fo.read()
        pixelStr = re.sub(r"[\n\t\s]*", "", pixelStr)
        count = 0

        while (count < 32):
            for y in range(0, 32):
                    for x in range(0, 32):
                        pixelPos = pixelStr[x+(y*32)]
                        canvas.SetPixel( x, y,
                                        d[pixelPos][0],
                                        d[pixelPos][1],
                                        d[pixelPos][2])
            canvas = self.matrix.SwapOnVSync(canvas)
            #self.usleep(microBPM/8) # main one, going to try another
            self.usleep(microBPM/12)
            headlessStr = pixelStr[1:]
            pixelStr = headlessStr + pixelStr[0]
            count += 1
            
        fo.close()

    def goRight(self, sheet):
        canvas = self.matrix.CreateFrameCanvas()
        sheetName = sheet
        fo = open('/home/pi/Desktop/pixelSheets/' + sheetName)
        pixelStr = fo.read()
        pixelStr = re.sub(r"[\n\t\s]*", "", pixelStr)
        count = 0

        while (count < 32):
            for y in range(0, 32):
                    for x in range(0, 32):
                        pixelPos = pixelStr[x+(y*32)]
                        canvas.SetPixel( x, y,
                                        d[pixelPos][0],
                                        d[pixelPos][1],
                                        d[pixelPos][2])
            canvas = self.matrix.SwapOnVSync(canvas)
            #self.usleep(microBPM/8) # MAIN
            self.usleep(microBPM/12)
            taillessStr = pixelStr[:-1]
            pixelStr =  pixelStr[-1:] + taillessStr
            count += 1
            
        fo.close()
        
    # Choosing specific scene
    # should add time factor
    def sceneFlipThrough(self, scene):
        canvas = self.matrix.CreateFrameCanvas()
        sceneName = scene
        while True:
            for file in sorted(os.listdir('/home/pi/Desktop/scenes/' + sceneName)):
                fo = open(os.path.join('/home/pi/Desktop/scenes/' + sceneName, file))
                pixelStr = fo.read()
                pixelStr = re.sub(r"[\n\t\s]*", "", pixelStr)

                print("filename: " + file)

                for y in range(0, 32):
                    for x in range(0, 32):
                        pixelPos = pixelStr[x+(y*32)]
                        canvas.SetPixel( x, y,
                                        d[pixelPos][0],
                                        d[pixelPos][1],
                                        d[pixelPos][2])
                canvas = self.matrix.SwapOnVSync(canvas)
                self.usleep((476190)/2)
                fo.close()

    # probably only flipped through once
    # 4 images usually make the entire scene
    def sceneFlipThroughCount(self, scene, maxFlips):
        canvas = self.matrix.CreateFrameCanvas()
        sceneName = scene
        flips = 0
        while (flips < maxFlips):
            for file in sorted(os.listdir('/home/pi/Desktop/scenes/' + sceneName)):
                fo = open(os.path.join('/home/pi/Desktop/scenes/' + sceneName, file))
                pixelStr = fo.read()
                pixelStr = re.sub(r"[\n\t\s]*", "", pixelStr)

                print("filename: " + file)

                for y in range(0, 32):
                    for x in range(0, 32):
                        pixelPos = pixelStr[x+(y*32)]
                        canvas.SetPixel( x, y,
                                        d[pixelPos][0],
                                        d[pixelPos][1],
                                        d[pixelPos][2])
                canvas = self.matrix.SwapOnVSync(canvas)
                self.usleep(microBPM*1.5)
                fo.close()
            flips += 1
        #self.usleep(9999999)
                

    def rndmKaskade(self, sheet):
        canvas = self.matrix.CreateFrameCanvas()
        sheetName = sheet
        
        fo = open('/home/pi/Desktop/pixelSheets/' + sheetName)
        pixelStr = fo.read()
        pixelStr = re.sub(r"[\n\t\s]*", "", pixelStr)
        count = 0

        while (count < 32):
            for x in range(0, 32):
                for y in range(0, 32):
                    pixelPos = pixelStr[x+(y*32)]
                    canvas.SetPixel( x, y,
                                     d[pixelPos][0],
                                     d[pixelPos][1],
                                     d[pixelPos][2])
                canvas = self.matrix.SwapOnVSync(canvas)
                self.usleep((microBPM)/8)

        self.usleep(999999)
        fo.close()

    # creates cool effect
    def kaskade(self, sheet):
        canvas = self.matrix.CreateFrameCanvas()
        sheetName = sheet
        
        fo = open('/home/pi/Desktop/pixelSheets/' + sheetName)
        pixelStr = fo.read()
        pixelStr = re.sub(r"[\n\t\s]*", "", pixelStr)
        count = 0

        while (count < 32):
            for x in range(0, 32):
                for m in range(0, (x+1)):
                    for y in range(0, 32):
                        pixelPos = pixelStr[m+(y*32)]
                        canvas.SetPixel( m, y,
                                         d[pixelPos][0],
                                         d[pixelPos][1],
                                         d[pixelPos][2])
                canvas = self.matrix.SwapOnVSync(canvas)
                self.usleep(microBPM/8)
                count += 1

        self.usleep(999999)
        fo.close()
