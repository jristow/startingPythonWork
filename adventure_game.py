# You are welcome to write and include any other Python files you want or need
# however your game must be started by calling the main function in this file.
from characterClass import Character
from random import random, choice

def intro():
    print("Welcome to the adventures of Hank the Goldendoodle. In today's escapade we join Hank as he tries to sneak past his human\nand steal the chicken carcass from the kitchen counter.")
    print("As Hank makes the harrowing journey from living room to kitchen he will need some assistance from you to make \nsome decisions.")
    print('\n')
    
def movementFunction(hero, enemy1, enemy2, enemy3, enemyListIn):
#This defines the basic function of making a move. Two possible outcomes are getting pats or running into an enemy.
    enemyList = enemyListIn
    lootOrEnemy = random()
    attackingEnemy = None
    if lootOrEnemy <= .6:
        newPats = hero.findLoot(20)
        print("The human gives you {} pats on the head. Who's a good boy?!".format(newPats))
    else:
        if enemyList == []:
            newPats = hero.findLoot(10)
            print("The human gives you {} pats on the head. Who's a good boy?!".format(newPats))
        else:
            attackingEnemy = choice(enemyList)
            attackSequence(hero, attackingEnemy)
            enemyList.remove(attackingEnemy)

#Defining the attack sequence which reads the enemies remaining 'health' to determine how long the while loop should run.
#
def attackSequence(hero, attackingEnemy):
    print("Oh no its {0}! {1}".format(attackingEnemy.getName(),attackingEnemy.getCatchphrase()))
    while attackingEnemy.getHealth() > 0:
        enemyTreatsLost = hero.attackDamage(20)
        heroTreatsLost = attackingEnemy.attackDamage(5)
        print('Attacking {}'.format(attackingEnemy.getName()))
        attackingEnemy.loseHealth(enemyTreatsLost)
        print('You take {0} treats from {1}! {2} treats left'.format(enemyTreatsLost, attackingEnemy.getName(), attackingEnemy.getHealth()))
        if attackingEnemy.getHealth() <= 0:
            print("You took all of the treats from {}.".format(attackingEnemy.getName()))
            break
        print('{} is attacking you!'.format(attackingEnemy.getName()))
        hero.loseHealth(heroTreatsLost)
        print('{0} takes {1} treats from you. {2} treats left'.format(attackingEnemy.getName(), heroTreatsLost, hero.getHealth()))
        if hero.getHealth() <= 0:
            print("Oh no you've lost all your treats! Better luck next time!")
            break
   

def main():
    intro()
    #This code segment initializes all of our characters for the game
    hank = Character('Hank', 60,"Cunning canine on the hunt for Chicken and pats!")
    jimmyRoboVac = Character('Jimmy the Robo Vac', 20, "Be careful or he'll suck down your tail!")
    mittensTheKitten = Character('Mittens the Kitten', 20, "This evil cat will do everything in her power to turn the human against you!")
    peteyTheParrot = Character('Petey the Parrot', 20, "He'll divebomb you for your treats!")
    
    enemyList = [jimmyRoboVac, mittensTheKitten, peteyTheParrot]
    
    for i in range(10):
        move = input('Take a step forward? (y/n): ')
        if move == 'y':
            movementFunction(hank, jimmyRoboVac, mittensTheKitten, peteyTheParrot, enemyList)
        else:
            print('The driving desire of chicken overcomes all hesitations and you step forward!')
            movementFunction(hank, jimmyRoboVac, mittensTheKitten, peteyTheParrot, enemyList)
            
    print("You made it to the kitchen! Unfortunately it looks like the human already threw out your chicken carcass...")
    print("I guess you'll have to settle for getting {0} pats on the head and ending with {1} treats.".format(hank.getLoot(), hank.getHealth()))
    
    
    
main()