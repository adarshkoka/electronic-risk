import time
import State
import Color
import multiprocessing
import ProjectHandler
import keyboard
import RPi.GPIO as GPIO
import os

DEBUG = True
num_players = 6
ind = 0
state = 0
stateInd = 0
lastStateInd = 0


def segEscape():
    global ind
    if keyboard.is_pressed('b'):
        ind = 0
    elif keyboard.is_pressed('x'):
        ind = 1
    elif keyboard.is_pressed('a'):
        ind = 2
    elif keyboard.is_pressed('i'):
        ind += 1
    
def ledCont(r, g, b):
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    GPIO.setup(23,  GPIO.OUT)
    GPIO.setup(10,  GPIO.OUT)
    GPIO.setup(22,  GPIO.OUT)
    
    GPIO.output(23, GPIO.LOW)
    GPIO.output(10, GPIO.LOW)
    GPIO.output(22, GPIO.LOW)
    
    
    if r:
        GPIO.output(10, GPIO.HIGH)
    if g:
        GPIO.output(22, GPIO.HIGH)
    if b:
        GPIO.output(23, GPIO.HIGH)
        
    
def updateRGB(color):
    #0: red
    #1: green
    #2: blue
    #3: cyan
    #4: magenta
    #5: yellow
    #6: white
    if color == 6:
        ledCont(1,0,0)
    elif color == 1:
        ledCont(0,1,0)
    elif color == 2:
        ledCont(0,0,1)
    elif color == 3:
        ledCont(0,1,1)
    elif color == 4:
        ledCont(1,0,1)
    elif color == 5:
        ledCont(1,1,0)
    else:
        ledCont(1,1,1)
    
    

def displayNumber(num, side):

	GPIO.setmode(GPIO.BCM)
	GPIO.setwarnings(False)

	GPIO.setup(5,  GPIO.OUT)
	GPIO.setup(6,  GPIO.OUT)
	GPIO.setup(27, GPIO.OUT)
	GPIO.setup(21, GPIO.OUT)
	GPIO.setup(20, GPIO.OUT)
	GPIO.setup(25, GPIO.OUT)
	GPIO.setup(24, GPIO.OUT)
	GPIO.setup(17, GPIO.OUT)
	GPIO.setup(26,  GPIO.OUT)
	
	GPIO.output(6, GPIO.LOW)
	GPIO.output(27, GPIO.LOW)
	GPIO.output(21, GPIO.LOW)
	GPIO.output(20, GPIO.LOW)
	GPIO.output(25, GPIO.LOW)
	GPIO.output(24, GPIO.LOW)
	GPIO.output(17, GPIO.LOW)
	GPIO.output(5, GPIO.LOW)
	GPIO.output(26,GPIO.LOW)
	
	GPIO.setup(18, GPIO.OUT)
	GPIO.setup(4, GPIO.OUT)
	
	if side == 1:
		GPIO.output(18, GPIO.HIGH)
		GPIO.output(4, GPIO.LOW)
	else:
		GPIO.output(4, GPIO.HIGH)
		GPIO.output(18, GPIO.LOW)
	
	if num == 9:
		#COUNTDOWN '9'
		GPIO.output(5, GPIO.HIGH)
		GPIO.output(6, GPIO.HIGH)
		GPIO.output(27, GPIO.HIGH)
		GPIO.output(26, GPIO.HIGH)
		GPIO.output(25, GPIO.HIGH)
		GPIO.output(24, GPIO.HIGH)
		GPIO.output(17, GPIO.HIGH)
	
	if num == 8:
		#COUNTDOWN '8'
		GPIO.output(5, GPIO.HIGH)
		GPIO.output(6, GPIO.HIGH)
		GPIO.output(21, GPIO.HIGH)
		GPIO.output(27, GPIO.HIGH)
		GPIO.output(26, GPIO.HIGH)
		GPIO.output(25, GPIO.HIGH)
		GPIO.output(24, GPIO.HIGH)
		GPIO.output(17, GPIO.HIGH)
		
	if num == 7:
		#COUNTDOWN '7'
		GPIO.output(5, GPIO.HIGH)
		GPIO.output(27, GPIO.HIGH)
		GPIO.output(17, GPIO.HIGH)
	
	if num == 6:
		#COUNTDOWN '6'
		GPIO.output(5, GPIO.HIGH)
		GPIO.output(6, GPIO.HIGH)
		GPIO.output(21, GPIO.HIGH)
		GPIO.output(26, GPIO.HIGH)
		GPIO.output(25, GPIO.HIGH)
		GPIO.output(24, GPIO.HIGH)
		GPIO.output(17, GPIO.HIGH)
	
	if num == 5:
		#COUNTDOWN '5'
		GPIO.output(5, GPIO.HIGH)
		GPIO.output(6, GPIO.HIGH)
		GPIO.output(26, GPIO.HIGH)
		GPIO.output(25, GPIO.HIGH)
		GPIO.output(24, GPIO.HIGH)
		GPIO.output(17, GPIO.HIGH)
	
	if num == 4:
		#COUNTDOWN '4'
		GPIO.output(6, GPIO.HIGH)
		GPIO.output(27, GPIO.HIGH)
		GPIO.output(26, GPIO.HIGH)
		GPIO.output(25, GPIO.HIGH)
		GPIO.output(17, GPIO.HIGH)
		
	if num == 3:
		#COUNTDOWN '3'
		GPIO.output(5, GPIO.HIGH)
		GPIO.output(6, GPIO.HIGH)
		GPIO.output(27, GPIO.HIGH)
		GPIO.output(25, GPIO.HIGH)
		GPIO.output(24, GPIO.HIGH)
		GPIO.output(17, GPIO.HIGH)
		
	if num == 2:
		#COUNTDOWN '2'
		GPIO.output(5, GPIO.HIGH)
		GPIO.output(6, GPIO.HIGH)
		GPIO.output(21, GPIO.HIGH)
		GPIO.output(27, GPIO.HIGH)
		GPIO.output(25, GPIO.HIGH)
		GPIO.output(24, GPIO.HIGH)
		
	if num == 1:
		#COUNTDOWN '1'
		GPIO.output(27, GPIO.HIGH)
		GPIO.output(17, GPIO.HIGH)

	if num == 0:
		#COUNTDOWN '80
		GPIO.output(5, GPIO.HIGH)
		#GPIO.output(6, GPIO.HIGH)
		GPIO.output(21, GPIO.HIGH)
		GPIO.output(27, GPIO.HIGH)
		GPIO.output(26, GPIO.HIGH)
		#GPIO.output(25, GPIO.HIGH)
		GPIO.output(24, GPIO.HIGH)
		GPIO.output(17, GPIO.HIGH)
		
		
def updateSevSegF(dig1, dig2):
    global ind
    localNum = ind
    while localNum == ind:
        try:
               time.sleep(0.005)
               displayNumber(dig1, 0)
               time.sleep(.008)
               displayNumber(dig2, 1)
               #time.sleep(.00001)
               segEscape()
        except:
            return
    print ('sevSegNum: ' + str(ind) + '\nlocalNum: ' + str(localNum))

def updateSevSeg(num):
    segEscape()
    strNum = str(num)
    if num > 9 and num < 100:
        dig1 = int(strNum[0])
        dig2 = int(strNum[1])
    elif num <= 9:
        dig1 = 0
        dig2 = int(strNum[0])
    else:
        dig1 = 9
        dig2 = 9
    
    #kill old thread if one exists
    #start new thread and updateSevSegF()
    updateSevSegF(dig1, dig2)
    
    if DEBUG:
        print('dig1: ' + str(dig1))
        print('dig2: ' + str(dig2))
        
        
def select(num):
    global state
    global stateInd
    global lastStateInd
    
    lastStateInd = stateInd
    stateInd = num
    print ('\nStateInd: ' + str(stateInd) + '\n')
    state = ProjectHandler.stateOf(num)
    stateUnits = state.getNumUnits()
    updateRGB(ProjectHandler.hardwareColor(stateInd))
    print('\nColor Selected: ' + str(ProjectHandler.hardwareColor(stateInd)) + '\n')
    updateSevSeg(stateUnits)
    
def increment():
    global state
    global stateInd
    
    stateUnits = state.getNumUnits()
    ProjectHandler.increment(stateInd)
    updateSevSeg(stateUnits + 1)
    
def decrement():
    global state
    global stateInd
    
    stateUnits = state.getNumUnits()
    ProjectHandler.increment(stateInd)
    updateSevSeg(stateUnits - 1)
    
    
def battle():
    global stateInd
    global lastStateInd
    
    ProjectHandler.battle(lastStateInd, stateInd)
    
    
def auto_assign(num):
    global state
    ProjectHandler.autoAssign(num)
    state = ProjectHandler.stateOf(0)
  

def main():
    #userNum = 69
    updateRGB(6)
    print('1')
    time.sleep(0.5)
    
    updateRGB(1)
    print('2')
    time.sleep(0.5)
    
    updateRGB(2)
    print('3')
    time.sleep(0.5)
    
    updateRGB(3)
    print('4')
    time.sleep(0.5)
    
    updateRGB(4)
    print('5')
    time.sleep(0.5)
    
    updateRGB(5)
    print('6')
    time.sleep(0.5)
    
    updateRGB(6)
    print('7')
    time.sleep(0.5)
    
    updateRGB(1)
    print('GO')
    time.sleep(0.5)
    
    auto_assign(6)
    #os.system('sudo -u pi aplay Intro.wav')
    keyboard.add_hotkey('a', lambda: select(0))
    keyboard.add_hotkey('b', lambda: select(1))
    keyboard.add_hotkey('i', lambda: increment())
    keyboard.add_hotkey('x', lambda: battle())
    
    select(0)
    
    keyboard.wait('esc')        #Reset Button                                                                     
        
        
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        GPIO.cleanup()
        print ("Program ended with Keyboard Interrupt")
