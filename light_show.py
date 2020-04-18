from samplebase import SampleBase
from light_manager import *
import pyaudio
import re
import os
import time

'''
    Attack On Dragon's Gate's Code
    
    Raspberry Pi + RGB Hat
    1 32x32 LED Matrix
    
'''
class LightShow(LightManager):
    def __init__(self, *args, **kwargs):
        super(LightShow, self).__init__(*args, **kwargs)
    
    # all the work is done here
    # self.functionCall(arguments)
    def run(self):
        self.showMyWork("64x64", 64)
        
        self.sceneFlipThroughCount("whiteMoonScene", 1)
        self.goRight("bomb_right_wb")
        self.sceneFlipThroughCount("finalScene", 1)
        self.usleep(999999999)

    # @param sheet - pixelSheet to show off
    # @param pixelMax - maxiumum # of pixels for 32x32 or 64x64
    def showMyWork(self, sheet, pixelMax):
        canvas = self.matrix.CreateFrameCanvas()
        sheetName = sheet
        
        fo = open('/home/pi/Desktop/pixelSheets/' + sheetName)
        pixelStr = fo.read()
        pixelStr = re.sub(r"[\n\t\s]*", "", pixelStr)
        count = 0

        for y in range(0, pixelMax):
            for x in range(0, pixelMax):
                pixelPos = pixelStr[x+(y*pixelMax)]
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
