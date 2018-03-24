class Flower:
    def __init__(self, name='Rose', petalNum = 5, price = 2.99):
        self.name = str(name)
        self.petalNumber = int(petalNum)
        self.price = float(price)
        
    def setName(self, name):
        self.name = str(name)
        
    def setPetals(self, petalNum):
        self.petalNumber = int(petalNum)
        
    def setPrice(self, price):
        self.price = float(price)
        
    def getName(self):
        return self.name
    
    def getPetals(self):
        return self.petalNumber
    
    def getPrice(self):
        return self.price
        
        