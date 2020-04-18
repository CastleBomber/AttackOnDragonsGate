from samplebase import SampleBase
import pyaudio
import re
import os
import time
from struct import unpack
import numpy as np


no_channels = 1
sample_rate = 44100
chunk = 4000
device = 2
p = pyaudio.PyAudio()
global stream
stream = p.open(format = pyaudio.paInt16,
                channels = no_channels,
                rate = sample_rate,
                input = True,
                frames_per_buffer = chunk,
                input_device_index = 2) # 2 || 4 hmm


'''
    returns height
    dictionary containing (freq perh.)
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
    print(height)
    #print(piff(16000))
    return height

height = {9:0,8:0,7:0,6:0,5:0,4:0,3:0,2:0,1:0,0:0}


def red(y):
    if(y < 2): return 0
    if(y > 13): return 255
    return 255/16*y

def green(y):
    if(y > 13): return 0
    if(y < 2): return 255
    return 19*(19/y)

def piff(val):
    return int(2*chunk*val/sample_rate)
    
'''

'''

class SoundManager(SampleBase):
    def __init__(self, *args, **kwargs):
        super(SoundManager, self).__init__(*args, **kwargs)
