import RPi.GPIO as GPIO
import time
#2  -> button input
#15  -> light 2 green
#7  -> light 2 blue
#8  -> light 2 red
#!5  -> light 1 green
#!6  -> light 1 blue
#7  -> light 1 red
#SEVEN SEGMENT
#5  -> 7seg A
#9  -> 7seg B
#17 -> 7seg C
#24 -> 7seg D
#21 -> 7seg E
#20 -> 7seg F
#6 -> 7seg G1
#25 -> 7seg G2

GPIO.cleanup()
try:
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(2,  GPIO.IN, pull_up_down=GPIO.PUD_UP)

    GPIO.setup(5,  GPIO.OUT)
    GPIO.setup(6,  GPIO.OUT)
    GPIO.setup(27, GPIO.OUT)
    GPIO.setup(21, GPIO.OUT)
    GPIO.setup(20, GPIO.OUT)
    GPIO.setup(25, GPIO.OUT)
    GPIO.setup(24, GPIO.OUT)
    GPIO.setup(17, GPIO.OUT)
    GPIO.output(6, GPIO.LOW)
    GPIO.output(27, GPIO.LOW)
    GPIO.output(21, GPIO.LOW)
    GPIO.output(20, GPIO.LOW)
    GPIO.output(25, GPIO.LOW)
    GPIO.setup(26,  GPIO.OUT)
    GPIO.output(24, GPIO.LOW)
    GPIO.output(17, GPIO.LOW)
    
    GPIO.setup(18, GPIO.OUT)
    GPIO.setup(4, GPIO.OUT)
    
    print ("Start")
    while True:
        
        #COUNTDOWN '8'
        GPIO.output(5, GPIO.HIGH)
        GPIO.output(6, GPIO.HIGH)
        GPIO.output(21, GPIO.HIGH)
        GPIO.output(27, GPIO.HIGH)
        GPIO.output(26, GPIO.HIGH)
        GPIO.output(25, GPIO.HIGH)
        GPIO.output(24, GPIO.HIGH)
        GPIO.output(17, GPIO.HIGH)
        
        #GPIO.setup(18, GPIO.HIGH)
        GPIO.output(4, GPIO.HIGH)
        
        time.sleep(1)
        
        GPIO.output(5, GPIO.LOW)
        GPIO.output(6, GPIO.LOW)
        GPIO.output(21, GPIO.LOW)
        GPIO.output(27, GPIO.LOW)
        GPIO.output(26, GPIO.LOW)
        GPIO.output(25, GPIO.LOW)
        GPIO.output(24, GPIO.LOW)
        GPIO.output(17, GPIO.LOW)
        
        #GPIO.output(18, GPIO.LOW)
        GPIO.output(4, GPIO.LOW)

        #COUNTDOWN '4'
        
        GPIO.output(6, GPIO.HIGH)
        GPIO.output(27, GPIO.HIGH)
        GPIO.output(26, GPIO.HIGH)
        GPIO.output(25, GPIO.HIGH)
        GPIO.output(17, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(6, GPIO.LOW)
        GPIO.output(27, GPIO.LOW)
        GPIO.output(26, GPIO.LOW)
        GPIO.output(25, GPIO.LOW)
        GPIO.output(17, GPIO.LOW)
        
        #COUNTDOWN '5'
        GPIO.output(5, GPIO.HIGH)
        GPIO.output(6, GPIO.HIGH)
        GPIO.output(26, GPIO.HIGH)
        GPIO.output(25, GPIO.HIGH)
        GPIO.output(24, GPIO.HIGH)
        GPIO.output(17, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(5, GPIO.LOW)
        GPIO.output(6, GPIO.LOW)
        GPIO.output(26, GPIO.LOW)
        GPIO.output(25, GPIO.LOW)
        GPIO.output(24, GPIO.LOW)
        GPIO.output(17, GPIO.LOW)
        
        #COUNTDOWN '6'
        GPIO.output(5, GPIO.HIGH)
        GPIO.output(6, GPIO.HIGH)
        GPIO.output(21, GPIO.HIGH)
        GPIO.output(26, GPIO.HIGH)
        GPIO.output(25, GPIO.HIGH)
        GPIO.output(24, GPIO.HIGH)
        GPIO.output(17, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(5, GPIO.LOW)
        GPIO.output(6, GPIO.LOW)
        GPIO.output(21, GPIO.LOW)
        GPIO.output(26, GPIO.LOW)
        GPIO.output(25, GPIO.LOW)
        GPIO.output(24, GPIO.LOW)
        GPIO.output(17, GPIO.LOW) 

except KeyboardInterrupt:
    GPIO.cleanup()  

GPIO.cleanup()
time.sleep(1)
GPIO.cleanup()
