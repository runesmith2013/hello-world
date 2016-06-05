#!/usr/bin/env python
import sys
import camera
import time
from twython import Twython

import picamera

camera = picamera.PiCamera()

def photo(number):
  camera.hflip = True
  camera.vflip = True
#  image = '/home/pi/myNas/image'+str(number)+'.jpg'
  image = '/home/pi/camera/image'+str(number)+'.jpg'
  camera.capture(image)
  print ('click') 
   
def tearDown():
  camera.close();    



