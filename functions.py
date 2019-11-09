from samplebase import SampleBase
#import driver
#from functions import LightShowHelper
import pyaudio
import re
import os

'''
    CastleBomber sigil/ show
'''
class LightShow(SampleBase):
    def __init__(self, *args, **kwargs):
        super(LightShow, self).__init__(*args, **kwargs)
    
##    def run(self):
##        self.rndmFlipThrough()
##        self.showMyWork()
##        
##        self.goLeft()
##        self.goRight()
##        self.rndmFlipThrough()

    '''
        Inside the folder 'pixelSheets' are "sketches"
        flips through images (have yet to work the ordering)
    '''
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

    '''
        Sigil goes left,
        set up count for 32 steps
        would slowly slide up if not stopped
    '''
    def goLeft(self):
        canvas = self.matrix.CreateFrameCanvas()
        fo = open('/home/pi/Desktop/pixelSheets/pixels_2bw')
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
            self.usleep(99999)
            headlessStr = pixelStr[1:]
            pixelStr = headlessStr + pixelStr[0]
            count += 1
            
        fo.close()

    def goRight(self):
        canvas = self.matrix.CreateFrameCanvas()
        fo = open('/home/pi/Desktop/pixelSheets/pixels_3bw')
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
            self.usleep(99999)
            taillessStr = pixelStr[:-1]
            pixelStr =  pixelStr[-1:] + taillessStr
            count += 1
            
        fo.close()

    def showMyWork(self):
        canvas = self.matrix.CreateFrameCanvas()
        fo = open('/home/pi/Desktop/pixelSheets/dragon')
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
        self.usleep(99999999)
        fo.close()

