import RPi.GPIO as GPIO
import time

led = 26

GPIO.setmode(GPIO.BCM)
GPIO.setup(led, GPIO.OUT)

pwm = GPIO.PWM(led, 200)
pwm.start(0)
duty = 0

while True:
    pwm.ChangeDutyCycle(duty)
    duty += 1
    time.sleep(0.02)

    if duty >= 100:
        duty = 0