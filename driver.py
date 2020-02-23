#!/usr/bin/env python
'''
sudo ./driver.py --led-rows=32 --led-cols=32  --led-brightness=60 --led-pwm-lsb-nanoseconds=300 --led-slowdown-gpio=2

    Code: Team Waveform
'''

from show_manager import ShowManager

if __name__ == "__main__":
    showManager = ShowManager()
