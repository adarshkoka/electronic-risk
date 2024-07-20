import Color as Col

class State:
    ID = -1
    numUnits = 0
    owner = Col.Color.RED
    def __init__(self, ID):
        self.ID = ID
        self.numUnits = 0
        self.owner = Col.Color.RED
        
    def __init__(self, ID, owner):
        self.ID = ID
        self.numUnits = 0
        self.owner = owner
    def getNumUnits(self):
        return self.numUnits
    def getOwner(self):
        return self.owner
    def getID(self):
        return self.ID
    
    def setNumUnits(self, num):
        self.numUnits = num
    
    def setOwner(self, own):
        self.owner = own
        
    def printy(self):
        print('State:' + str(self.ID))
        print('\tNumUnits: ' + str(self.numUnits))
        print('\tOwner: ' + str(self.owner))
