#!/usr/bin/env python
'''
sudo ./driver.py --led-rows=32 --led-cols=32  --led-brightness=40 --led-pwm-lsb-nanoseconds=300 --led-slowdown-gpio=2
'''
from samplebase import SampleBase
import pyaudio
import re
import os
import time
from functions import LightShow
#from functions import LightShow.goRight
        

if __name__ == "__main__":
    lightShow_driver = LightShow()
    #lightShow_driver.goRight("bomb_right_wb")
    if (not lightShow_driver.process()):
        lightShow_driver.print_help()
