#!/usr/bin/env python
'''
sudo ./raiseYourHandsUp.py --led-rows=32 --led-cols=32  --led-brightness=78 --led-pwm-lsb-nanoseconds=300 --led-slowdown-gpio=2
'''
from samplebase import SampleBase
from led_functions import *
import pyaudio
from functions import *
from layer2 import *
from Sigil import *
import re


d = dict()
d = {"0": [0x0, 0x0, 0x0],
     "1": [255, 0x0, 255],
     "2": [0x0, 0x0, 255],
     "3": [0x0, 255, 255],
     "4": [0x0, 255, 0x0],
     "5": [255, 255, 0x0],
     "6": [255,0xBE, 0x0],
     "7": [255, 0x0, 0x0],
     "9": [255, 255, 255]}

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

'''
'''
class VolumeBars(SampleBase):
    def __init__(self, *args, **kwargs):
        super(VolumeBars, self).__init__(*args, **kwargs)

    def run(self):
        fo = open("pixels_b", "r")
        pixelStr = fo.read()
        pixelStr = re.sub(r"[\n\t\s]*", "", pixelStr)
        
        canvas = self.matrix.CreateFrameCanvas()
        while True:
            for y in range(0, 32):
                for x in range(0, 32):
                    pixelPos = pixelStr[x+(y*32)]
                    canvas.SetPixel( x, y,
                                     d[pixelPos][0],
                                     d[pixelPos][1],
                                     d[pixelPos][2])
            canvas = self.matrix.SwapOnVSync(canvas)
            self.usleep(555555)
            fo.close() 

                   



# Main function
if __name__ == "__main__":
    led_driver = VolumeBars()   
    if (not led_driver.process()):
        led_driver.print_help()

