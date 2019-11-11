import functions
from functions import LightShowHelper
import pyaudio
import re
import os

#this is CHILD class
class ChildClass(LightShowHelper):
    def test1(self):
        self.testFunc()

if __name__ == "__main__":
    test = ChildClass()
    test.test1()

