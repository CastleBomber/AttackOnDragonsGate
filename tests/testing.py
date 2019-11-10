import functions
from functions import LightShowHelper
#from functions import *
import pyaudio
import re
import os

class TestClass(LightShowHelper):
    def test1(self):
        self.testFunc()

if __name__ == "__main__":
    test = TestClass()
    test.test1()

