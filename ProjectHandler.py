import random
import State
import Color
import time
import pygame
import os

#------------------------------------#
#          Global Variables          #
#------------------------------------#



DEBUG = True
selected_state = None   #The last selected state, indicated by select button; on which to perform operations on
stateUnits = [0] * 42
stateOwners = [0] * 42
states = [0] * 42
win_status = False



#------------------------------------#
#          Utility Functions         #
#------------------------------------#
def checkWin():
    global win_status
    if len(set(stateOwners)) == 1:
        win_status = True
        os.system('sudo -u pi aplay Intro.wav')
        if DEBUG:
            print("GAME WON")
    else:
        win_status = False
        
def colorOf(index):
    switcher = {
        1: Color.Color.RED,
        2: Color.Color.GREEN,
        3: Color.Color.BLUE,
        4: Color.Color.YELLOW,
        5: Color.Color.PURPLE,
        6: Color.Color.WHITE,
        0: Color.Color.NULL
        }
    return switcher.get(index, Color.Color.NULL)

def intOfColor(color):
    switcher = {
        Color.Color.RED : 1,
        Color.Color.GREEN: 2,
        Color.Color.BLUE : 3,
        Color.Color.YELLOW : 4,
        Color.Color.PURPLE : 5,
        Color.Color.WHITE : 6,
        Color.Color.NULL : 0
        }
    return switcher.get(color, 0)

def hardwareColor(index):
    #state = stateOf(index)
    #return intOfColor(state.getOwner())
    #print ('stateOwners[index]: ' + str(stateOwners[index]))
    return stateOf(index).getOwner()

def autoAssign(numPlayers):
    global stateUnits
    global stateOwners
    print(str(numPlayers))
    aux = list(range(len(stateUnits)))
    terr = 0
    currentPlayerNum = 1
    state = 0
    while aux:
        if terr == 42:
            break
        posit = random.randrange(len(aux))
        index = aux[posit]
        del aux[posit]
        stateUnits[index] = 1
        stateOwners[index] = currentPlayerNum
        state = State.State(index, currentPlayerNum)
        state.setNumUnits(1)
        states[index] = state
        
        
        currentPlayerNum = currentPlayerNum + 1
        if currentPlayerNum == numPlayers + 1:
            currentPlayerNum = 1
        terr = terr + 1
				
def rollDie():
    rand = random.randint(1,6)
    return rand

def battle(stateAttInd, stateDefInd):
    #Input: Attacking state and defending state
    #Output: Modify contents of stateAtt, stateDef, so that they reflect battle outcome
    
    #Always take the greatest number of units which can be assigned in order to speed up gameplay
    stateAtt = stateOf(stateAttInd)
    stateDef = stateOf(stateDefInd)
    
    numUnitsAtt = stateAtt.getNumUnits()
    if numUnitsAtt < 2:
        print('NOT ENOUGH UNITS ATTACKING')
        return
    if stateAtt.getOwner() == stateDef.getOwner():
        print('SAME COLOR\n')
        os.system('sudo -u pi aplay Wrong.wav')
        return
    
    numUnitsDef = stateDef.getNumUnits()
    attTotal = numUnitsAtt
    defTotal = numUnitsDef
    attackDice = []
    defenseDice = []
    attackLost = 0
    defenseLost = 0
    if (numUnitsAtt > 3):
        numUnitsAtt = 3 
    if (numUnitsDef > 2):
        numUnitsDef = 2
    for i in range(numUnitsAtt):
        attackDice.append(rollDie())
    for i in range(numUnitsDef):
        defenseDice.append(rollDie())
    attackDice = sorted(attackDice)
    defenseDice = sorted(defenseDice)
    attackDice.reverse()
    defenseDice.reverse()
    if (DEBUG):
        print ('attackDice: ' + str(attackDice))
        print ('defenseDice: ' + str(defenseDice))
    for i in range(len(defenseDice)):
        if attackDice[i] > defenseDice[i]:
            defenseLost += 1
        else:
            attackLost += 1
    attTotal -= attackLost
    defTotal -= defenseLost
    if defTotal < 1:
        attOwner = stateAtt.getOwner()
        stateDef.setOwner(attOwner) 
        attTotal -= 1
        defTotal = 1
        checkWin()
    
    stateAtt.setNumUnits(attTotal)
    stateDef.setNumUnits(defTotal)
    
    updateState(stateAtt)
    updateState(stateDef)


    if attackLost > 0:
        if defenseLost > 0:
            print('draw\n')
            os.system('sudo -u pi aplay BattleDraw.wav')
        else:
            print('loss\n')
            os.system('sudo -u pi aplay BattleLoss.wav')
    else:
        print('victory\n')
        os.system('sudo -u pi aplay BattleVictory.wav')
        
        
        

def stateOf(index):
    global stateUnits
    global stateOwners
    global states
    #ret = State.State(str(index), colorOf(stateOwners[index]))
    #ret.setNumUnits(stateUnits[index])
    ret = states[index]
    print ('Selected State: ' + str(ret.getID()) + '\n')
    return ret
 
def increment(ind):
    state = stateOf(ind)
    if (state != None):
        if (DEBUG):
            print("State " + str(state.getID()) + " Increment\n")
        state.numUnits = state.numUnits + 1 

def decrement(ind):
    state = stateOf(ind)
    if (state != None):
        if (DEBUG):
            print("State " + str(state.getID()) + " Decrement\n")
        state.numUnits = state.numUnits - 1 
    

def updateState(state):
    global stateUnits
    global stateOwners
    global states
    
    index = int(state.getID())
    stateUnits[index] = state.getNumUnits()
    stateOwners[index] = intOfColor(state.getOwner())
    states[index] = state
    

#------------------------------------#
#          Main Function             #
#------------------------------------#
    
    
def main():
    if (DEBUG):
        autoAssign(6)  #Initialize states to 42 blank states
        print(stateUnits)
        print(stateOwners)
        print("R: " + str(stateOwners.count(1)) + '\n')
        print("G: " + str(stateOwners.count(2)) + '\n')
        print("B: " + str(stateOwners.count(3)) + '\n')
        print("Y: " + str(stateOwners.count(4)) + '\n')
        print("P: " + str(stateOwners.count(5)) + '\n')
        print("W: " + str(stateOwners.count(6)) + '\n')
    state0 = stateOf(0)
    state1 = stateOf(1)
    increment(state0)
    increment(state1)
    #state1.setNumUnits(3)

    state0.printy()
    state1.printy()
    battle(state0, state1)
    state0.printy()
    state1.printy()

    updateState(state0)
    updateState(state1)
    print(stateUnits)
    print(stateOwners)
    
#main()

    
    
    

    
