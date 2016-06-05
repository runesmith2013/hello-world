#!/usr/bin/env python
import sys
import camera
import time
from twython import Twython

tweetStr = 'Welcome to Twitter!'

CONSUMER_KEY = '0f6ZXS1t1VZg7cRvBvPA0xMLD'
CONSUMER_SECRET = 'yWdJn0XkzP5UyOpoo18upxFTgaoxH6rA1casswD2bUQ2cAYqE9'
ACCESS_TOKEN = '701409275822940162-PFKG3w0VUioZOvnK7M9n3JdIswX84hI'
ACCESS_SECRET = 'wd2R88vCrq0IufVooQMbUyL8uF1SZsHXguhQ3S9zdZDd9'

api = Twython(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_SECRET)
 
print 'hello'

camera.photo(0)
photo = open ('/home/pi/camera/image0.jpg','rb')
response = api.upload_media(media=photo)
message = 'Photo' + str(i) 
api.update_status(status=message, media_ids=[response['media_id']])
print 'Uploaded '+ message  
time.sleep(10)
  
