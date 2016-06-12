import camera
import time
import twitterClient


for i in range(10):
  picture = camera.photo()
  twitterClient.postToTwitter(picture)
  time.sleep(1)

camera.tearDown()