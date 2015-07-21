# Hello World program in Python
#2015-7-21
import random

ourNum = random.randint(10, 100)
print "hello welcome to play number game. \n You can input your number from 10 to 100, then compare your number with my number. If you number is right, you are win.\n"
print "Please input number of your think."
inputNum = input()

def compareNum(inputNum, ourNum):
    while True:
        if inputNum == ourNum:
            print "You are win"
            break
        elif inputNum > ourNum:
            print "Your number is larger than ourNum"
        elif inputNum < ourNum:
            print "Your number is smaller than ourNum"
        print "Please input number of your think"
        inputNum = input()

compareNum(inputNum, ourNum)


