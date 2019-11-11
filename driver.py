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
     "6": [255,0xBE, 0x0], # Orange
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


# chunk must be a multipe of 8
# if chunk is too small program will crash
# with error message: [Error Input overflowed]
# device 2 is usb audio
no_channels = 1
sample_rate = 44100
chunk = 4000
device = 2

p = pyaudio.PyAudio()

stream = p.open(format = pyaudio.paInt16,
                channels = no_channels,
                rate = sample_rate,
                input = True,
                frames_per_buffer = chunk,
                input_device_index = 2) # 2 || 4 hmm

'''
    returns height
    dictionary containing freq?
'''
def calculate_levels(data, chunk, sample_rate):
    data = unpack("%dh"%(len(data)/2),data)
    data = np.array(data, dtype='h')
    
    # Apply FFT - real data
    fourier = np.fft.rfft(data)
    # Remove last element in array to make it the same size as chunk
    fourier = np.delete(fourier, len(fourier)-1)
    # Find average 'amplitude' for specific frequency ranges in Hz
    power = np.abs(fourier)
    height[0] = int(np.mean(power[piff(9000):piff(16000):1])/75)
    height[1] = int(np.mean(power[piff(7000):piff(10000):1])/75)
    height[2] = int(np.mean(power[piff(5000):piff(7000):1])/75)
    height[3] = int(np.mean(power[piff(2000):piff(5000):1])/75)
    height[4] = int(np.mean(power[piff(1500):piff(2000):1])/100)
    height[5] = int(np.mean(power[piff(1000):piff(1500):1])/200)
    height[6] = int(np.mean(power[piff(500):piff(1000):1])/350)
    height[7] = int(np.mean(power[piff(250):piff(500):1])/500)
    height[8] = int(np.mean(power[piff(150):piff(250):1])/750)
    height[9] = int(np.mean(power[piff(100):piff(150):1])/1000)
    print(height)#for testing purposes
    return height

height = {9:0,8:0,7:0,6:0,5:0,4:0,3:0,2:0,1:0,0:0}

songBPM = 126
microBPM = (60000/songBPM)*(1000) # ms, used for usleep

'''
    CastleBomber sigil/ show
'''
class LightShow(SampleBase):
    def __init__(self, *args, **kwargs):
        super(LightShow, self).__init__(*args, **kwargs)
    
    def run(self):
        
        
        # Act 1
        #self.goLeft("bomb_left_bw")
        #self.sceneFlipThroughCount("thoughtsScene", 1)
        #self.goLeft("bomb_left_eb")
        #self.sceneFlipThroughCount("moonScene", 1)
        #self.goLeft("bomb_left_wb")
        #self.sceneFlipThroughCount("moonScene", 1)
        
        #self.goRight("bomb_right_bw")
        #self.sceneFlipThroughCount("moonScene", 1)
        #self.goRight("bomb_right_eb")
        #self.sceneFlipThroughCount("moonScene", 1)
        #self.goRight("bomb_right_wb")
        #self.sceneFlipThroughCount("moonScene", 1)

        #print(time.clock())
        #self.kaskade("dragon")
        #print(time.clock())
        #self.rndmKaskade("dragon")
        #self.sceneFlipThrough()
        #self.rndmFlipThrough()
        self.showMyWork("tori_1")


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
            self.usleep(microBPM/8)
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
            self.usleep(microBPM/8)
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
                self.usleep(microBPM)
                fo.close()
            flips += 1
        self.usleep(9999999)
                

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
                self.usleep((microBPM)/4)

        self.usleep(999999)
        fo.close()

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
                self.usleep(microBPM/4)
                count += 1

        self.usleep(9999999)
        fo.close()
        

        

if __name__ == "__main__":
    lightShow_driver = LightShow()
    if (not lightShow_driver.process()):
        lightShow_driver.print_help()
