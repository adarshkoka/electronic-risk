import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
'''
GPIO.setup(2,  GPIO.IN, pull_up_down=GPIO.PUD_UP)
while True:
        buttonDown = GPIO.input(2)
        if buttonDown == False:
            print "Button Pressed"
            time.sleep(.2)
'''

GPIO.setup(15,GPIO.OUT)
print "LED on"
GPIO.output(15,GPIO.HIGH)
time.sleep(1)
print "LED off"
GPIO.output(15,GPIO.LOW)

