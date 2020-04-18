from light_show import LightShow
from team_show import TeamShow # troubles w/ TS && SS both imported
from sound_show import SoundShow

class ShowManager():
    def __init__(self):
        lightShow = LightShow()
        lightShow.process();
        
        #teamShow = TeamShow()
        #teamShow.process();
        
        #soundShow = SoundShow()
        #soundShow.process();
        
