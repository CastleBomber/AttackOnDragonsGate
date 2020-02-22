#!/usr/bin/env python
'''
sudo ./driver.py --led-rows=32 --led-cols=32  --led-brightness=60 --led-pwm-lsb-nanoseconds=300 --led-slowdown-gpio=2

    Code: Team Waveform
'''

from show_manager import ShowManager
from light_show import LightShow
#from team_show import TeamShow # troubles w/ TS && SS both imported
#from sound_show import SoundShow
from samplebase import SampleBase
import pyaudio
import re
import os
import time



from struct import unpack
import numpy as np


        

if __name__ == "__main__":
    showManager = ShowManager()

