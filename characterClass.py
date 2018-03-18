from random import randrange

class Character:
    def __init__(self, name, healthpoints, catchPhrase):
        self.name = name
        self.health = int(healthpoints)
        self.catchphrase = catchPhrase
        self.loot = 0
        
    def getName(self):
        return self.name
        
    def getHealth(self):
        return self.health
    
    def getLoot(self):
        return self.loot
    
    def getCatchphrase(self):
        return self.catchphrase
    
    def findLoot(self, maxLoot):
        newLoot = randrange(0,maxLoot)
        self.loot = self.loot + newLoot
        return newLoot
    
    def attackDamage(self, maxDamage):
        return randrange(0,maxDamage)
    
    def loseHealth(self, healthToLose):
#        if healthToLose >= self.health:
#            raise ValueError("You have died!")
        self.health = self.health - healthToLose
        return self.health