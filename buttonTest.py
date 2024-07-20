import RPi.GPIO as GPIO
import time
import Adafruit_MCP4725

def check():
    input_state = GPIO.input(21)
    return input_state
def getInput(input):
    brk = True


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(21,  GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.add_event_detect(21, GPIO.FALLING, callback=getInput, bouncetime=200)

while True:
    print('fuck bottomText')
    if (check()):
        break
        print('broken!')