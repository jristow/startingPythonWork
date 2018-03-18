#This program builds a list of user inputs and tells if it is a unique list

def getUserInput():
    print('This program tests if the sequence of positive numbers you input are unique')
    print('Enter -1 to quit')
    
    inputList = []
    userInput = int(input('Please the first number: '))
    while userInput != -1:
        inputList.append(userInput)
        userInput = int(input('Enter the next number: '))
    return inputList

def processList( list ):
    inputList = list
    countList = []
    for i in inputList:
        countList.append(inputList.count(i))
    countList.sort(reverse = True)
    if countList[1] == 1:
        return True
    else:
        return False
    
def printUniqueness(list, isUnique):
    if isUnique == True:
        print('The sequence {} is unique!'.format(list))
    else:
        print('The sequence {} is not unique.'.format(list))

def main():
    inputList = getUserInput()
    isUnique = processList(inputList)
    printUniqueness(inputList, isUnique)