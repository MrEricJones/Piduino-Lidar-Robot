##
## My first attempt at using onboard gpio pins to drive pwm signals
## and it was an epic fail because the rpi uses a software driven 
## clock that isnt consistent when the rpi is doing anything else.
## This causes a huge amount of jitter in the servos and victor motor
## controllers.
##

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(18, GPIO.OUT)

p = GPIO.PWM(18, 50)

p.start(7.5)

try:
    while True:
        p.ChangeDutyCycle(7.5)
##        time.sleep(1)
##        p.ChangeDutyCycle(6.6)
##        time.sleep(1)
##        p.ChangeDutyCycle(7.2)
##        time.sleep(1)
##        p.ChangeDutyCycle(7.83)
##        time.sleep(1)

except KeyboardInterrupt:
    p.stop()
    GPIO.cleanup()
