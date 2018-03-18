''' This program will allow a user to enter a password length then randomly build a password of that length.

Step 1: Get user input to identify length of password
Step 2: Loop that selects characters from a list and assigns them into a string that will be returned
as the password. Loop length will be defined by user input (for i in range(n))
    -Will need random.choice to select a number.
    -Can either use ASCII values of the characters or build an alphabet list to select from
    -Need to include lower and uppercase letters only. No limit on needing specific numbers of either
Step 3: Return the password generated to the user


'''
from random import choice

def getUserInput():
    passLength = int(input('How many characters for your password? '))
    return passLength

def buildPassword(length):
    abcString = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    password = ''
    for i in range(length):
        password = password + choice(abcString)
    return password


def main():
    input = getUserInput()
    password = buildPassword(input)
    print(password)
    
    
main()
