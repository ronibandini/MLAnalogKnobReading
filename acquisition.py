#!/usr/bin/env python

# Image acquisition script for Machine Learning 
# Take pictures using Raspberry Pi cam every X seconds and save random file names
# Roni Bandini @ronibandini
# MIT License
# October 2022

# Usage python3 acquisition.py

from picamera import PiCamera
from time import sleep
import random
import string

myCounter=1
camera = PiCamera()
camera.resolution = (1640, 1232)
print("Knob image acquisition script started")
print("")

while True:
        print("Taking pic #"+str(myCounter))        
        camera.capture(random.choice(string.ascii_letters)+random.choice(string.ascii_letters)+str(myCounter)+'.jpg')
        myCounter=myCounter+1
        if myCounter==21:
            break
        print("Move the knob")
        sleep(4)

print("")
print("Finished")
