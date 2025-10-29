import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(26, GPIO.OUT)
state = 1

while True:
    GPIO.output(26, state)
    state = not state
    time.sleep(0.5)
