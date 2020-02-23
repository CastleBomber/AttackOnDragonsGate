from samplebase import SampleBase
from sound_manager import *
import pyaudio
import re
import os
import time
from struct import unpack
import numpy as np
##chop


'''
    16x32
'''
class TeamShow(SoundManager):
    def __init__(self, *args, **kwargs):
        super(TeamShow, self).__init__(*args, **kwargs)

        
    def run(self):
        self.teamWaveForm()
        
    # 16x32
    def teamWaveForm(self):
        canvas = self.matrix.CreateFrameCanvas()
        while True:
            data = stream.read(chunk)
            self.usleep(5000)
            height = calculate_levels(data, chunk, sample_rate)
            i=0
            for x in range(1,31,3):
                for y in range(0,16):
                    if(y < height[i]):
                        canvas.SetPixel(x,y,red(y),green(y),0)
                        canvas.SetPixel(x+1,y,red(y),green(y),0)
                        canvas.SetPixel(x+2,y,red(y),green(y),0)
                    else:
                        canvas.SetPixel(x,y,0,0,0)
                        canvas.SetPixel(x+1,y,0,0,0)
                        canvas.SetPixel(x+2,y,0,0,0)
                i+=1
            canvas = self.matrix.SwapOnVSync(canvas)

        
