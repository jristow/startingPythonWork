# This program will simulate betting on games of roulette
from random import randrange


def getSetupInfo():  #This function takes in the users initial inputs and returns them for assignment to variables  
    initialDollars = int(input("Enter the number of dollars you start with: "))
    numberOfSpins = int(input("Enter the number of spins you will play: "))
    betAmount = int(input("Enter how many dollars you will bet for each spin: "))
    return initialDollars, numberOfSpins, betAmount

def getUserStrategy(): #This function explains the betting strategies and gets/returns the users choice
    print("Choose one of the following betting strategies\n")
    print('-Bet on a (s)ingle number (pays 35 to 1)')
    print('-Bet on (e)ven or odd numbers (pays 1 to 1)')
    print('-Bet on a (d)ozen numbers (pays 2 to 1)')
    strategy = input('Enter your strategy choice (s, e or d): ')
    return strategy

def betChoice(strategy): #This function takes the users betting strategy choice and gets the appropriate details for their actual bet placement
    if strategy == 's':
        userChoice = int(input('Enter the single number you wish to bet on (00 or 0 to 36): '))
        if userChoice == 00: #Setting 00 to be the value 37
            userChoice = 37
    elif strategy == 'e':
        userChoice = input('Enter if you want to bet on (e)ven or (o)dd numbers: ')
    elif strategy == 'd':
        userChoice = int(input('Enter 1 to bet on numbers 1-12, 2 for numbers 13-24 or 3 for numbers 25-36: '))
    return userChoice

def rouletteGame(dollars, numberSpins, betAmount, strategy, betChoice ): #This function compiles the results of the games as they are played
    dollarsRemaining = dollars
    gameCounter = 0
    betResult = 0
    wins = 0
    losses = 0
    for i in range(numberSpins): #In this for loop we evaluate what the strategy is and then execute the correct roulette spin
        if strategy == 'e': 
            betResult = evenOddRouletteSpin(betAmount, betChoice)
            if betResult > 0:
                wins += 1
            else:
                losses += 1
        elif strategy == 's':
            betResult = singleNumRouletteSpin(betAmount, betChoice)
            if betResult > 0:
                wins += 1
            else:
                losses += 1
        elif strategy == 'd':
            betResult = dozenNumRouletteSpin(betAmount, betChoice)
            if betResult > 0:
                wins += 1
            else:
                losses += 1
        dollarsRemaining = dollarsRemaining + betResult
        gameCounter += 1
        if dollarsRemaining == 0:
            break
    return dollarsRemaining, gameCounter, wins, losses
        
            
def oneSpin():
    return randrange(0,38)
 
def evenOddRouletteSpin(betAmount, betChoice): #This function evaluates the result of a spin when the user selected even/odd as their betting strategy
    spin = oneSpin()
    betResult = 0
    if spin == 0 or spin == 37: #This case is if either 0 or 00 comes up (37 is defined to be 00 in this program)
        betResult = -betAmount
    elif betChoice == 'e':
        if spin % 2 == 0:
            betResult = betAmount #Because the return on even/odd is 1 to 1, there is no multiplier like in the other two cases
        else:
            betResult = -betAmount
    elif betChoice == 'o':
        if spin % 2 != 0:
            betResult = betAmount
        else:
            betResult = -betAmount
    return betResult

def singleNumRouletteSpin(betAmount, betChoice): #This function evaluates the result of a spin when the user selected the single number as their betting strategy
    spin =  oneSpin()
    betResult = 0
    if spin == betChoice:
        betResult = betAmount * 35 #This calculates the amount the user would win for a correct choice on one spin
    else:
        betResult = -betAmount
    return betResult

def dozenNumRouletteSpin(betAmount, betChoice): #This function evaluates the result of a spin when the user selected the dozens as their betting strategy
    spin = oneSpin()
    betResult = 0
    if spin == 0 or spin == 37: #This is the case where either 0 or 00 come up (37 is defined to be 00 in this program)
        betResult = -betAmount
    elif spin < 13:
        if betChoice == 1:
            betResult = betAmount * 2 #This calculates the 2 to 1 return for a correct choice on the dozens betting strategy
        else:
            betResult = -betAmount
    elif spin < 25:
        if betChoice == 2:
            betResult = betAmount * 2
        else:
            betResult = -betAmount
    elif spin < 37:
        if betChoice == 3:
            betResult = betAmount * 2
        else:
            betResult = -betAmount
    return betResult
        
def printOutcome(gameCounter, wins, losses, dollarsRemaining, initialDollars):
    print("After {} games".format(gameCounter))
    print("Wins: {0} ({1:0.1%})".format(wins, wins/gameCounter))
    print("Losses: {0} ({1:0.1%})".format(losses, losses/gameCounter))
    print("Ending bank: ${0}".format(dollarsRemaining))
    print("Net winnings: ${0}".format(dollarsRemaining - initialDollars))

def main():
    initialDollars, numberOfSpins, betAmount = getSetupInfo()
    strategy = getUserStrategy()
    userBetChoice = betChoice(strategy)
    dollarsRemaining, gameCounter, wins, losses = rouletteGame(initialDollars, numberOfSpins, betAmount, strategy, userBetChoice)
    printOutcome(gameCounter, wins, losses, dollarsRemaining, initialDollars)
    
main()