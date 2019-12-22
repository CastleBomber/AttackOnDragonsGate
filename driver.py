#!/usr/bin/env python
'''
sudo ./driver.py --led-rows=32 --led-cols=32  --led-brightness=40 --led-pwm-lsb-nanoseconds=300 --led-slowdown-gpio=2
'''
from light_show import LightShow
        

if __name__ == "__main__":
    lightShow_driver = LightShow()
    if (not lightShow_driver.process()):
        lightShow_driver.print_help()
