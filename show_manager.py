from light_show import LightShow
#from team_show import TeamShow #  <--- troubles w/ TS && SS both imported
from sound_show import SoundShow # <---

from samplebase import SampleBase
import pyaudio
import re
import os
import time
from struct import unpack
import numpy as np


class ShowManager():
    
    def __init__(self):
    
        #lightShow = LightShow()
        #lightShow.process();
        
        soundShow = SoundShow()
        soundShow.process();
        
