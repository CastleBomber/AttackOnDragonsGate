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


class LightManager(SampleBase):
    def __init__(self, *args, **kwargs):
        super(LightManager, self).__init__(*args, **kwargs)
