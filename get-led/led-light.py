import RPi.GPIO as GPIO
import time

led = 26
button = 6
state = 0

GPIO.setmode(GPIO.BCM)
GPIO.setup(led, GPIO.OUT)
GPIO.setup(button, GPIO.IN)

while True:
    GPIO.output(led, not GPIO.input(button))
