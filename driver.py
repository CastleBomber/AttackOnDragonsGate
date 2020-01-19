#!/usr/bin/env python
'''
sudo ./driver.py --led-rows=32 --led-cols=32  --led-brightness=60 --led-pwm-lsb-nanoseconds=300 --led-slowdown-gpio=2

    Code: Team Waveform
'''
from light_show import LightShow
from team_show import TeamShow
from sound_show import SoundShow
from samplebase import SampleBase
import pyaudio
import re
import os
import time
        

if __name__ == "__main__":
    #lightShow = LightShow()
    teamShow = TeamShow()
    #soundShow = SoundShow()
    if (not soundShow.process()):
        soundShow.print_help()
#    if (not lightShow.process()):
#        lightShow.print_help()
