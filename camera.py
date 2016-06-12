#!/usr/bin/env python
import sys
import camera
import time
from twython import Twython

import picamera

camera = picamera.PiCamera()
camera.hflip = True
camera.vflip = True

def photo():
  timestamp = time.time()
  image = '/home/pi/camera/image'+str(timestamp)+'.jpg'
  camera.capture(image)
  print ('click click')
  return image

def tearDown():
  camera.close();    



