from picamera import PiCamera
from time import sleep
from datetime import datetime

camera = PiCamera()

camera.start_preview()

dt = datetime.now()
ts = datetime.timestamp(dt)
name = "/home/pi/Pictures/{}.jpg".format(ts)

camera.capture(name)
camera.stop_preview()
