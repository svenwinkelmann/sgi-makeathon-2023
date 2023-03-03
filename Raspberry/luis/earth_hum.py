import RPi.GPIO as GPIO
import time

chanel = 21
GPIO.setmode(GPIO.BCM)
GPIO.setup(chanel, GPIO.IN)

def callback(chanel):
    if GPIO.input(chanel):
        print("No water detected")
    else:
        print("Water detected")

GPIO.add_event_detect(chanel, GPIO.BOTH, bouncetime=300)
GPIO.add_event_callback(chanel, callback)

while True:
    time.sleep(1)