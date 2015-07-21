# Hello World program in Python
# 2015-7-21
import random

ourNum = random.randint(10, 1000)
print "hello welcome to play number game. \n You can input your number from 10 to 1000, then compare your number with my number. If you number is right, you are win.\n"
print "Please input number of your think."
inputNum = input()


def guessNum(inputNum, ourNum):
    times = 0
    while True:
        if inputNum == ourNum:
            print "I get your number with %d times" % (times,)
            break
        elif inputNum != ourNum:
            print "let me try again"
            ourNum = random.randint(10, 1000)
            print "I guess number is %d" % (ourNum,)
        times = times + 1


def compareNum(inputNum, ourNum):
    while True:
        if inputNum == ourNum:
            print "You are win"
            print "Please input your number from 10 to 1000, I guess it with how much times"
            inputNum = input()
            ourNum = random.randint(10,1000)
            guessNum(inputNum, ourNum)
            break
        elif inputNum > ourNum:
            print "Your number is larger than ourNum"
        elif inputNum < ourNum:
            print "Your number is smaller than ourNum"
        print "Please input number of your think"
        inputNum = input()

compareNum(inputNum, ourNum)