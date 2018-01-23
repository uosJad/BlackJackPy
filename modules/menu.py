from modules.gameRun import *
from classes.player import *

def runMenu():
    inp = -1;
    while True:
        printMenu();
        inp = input();
        if inp == 1:
            print('')
            runRound()
        elif inp == 2:
            return
        else:
            print("Not a valid entry")


def runHitMenu(deck, player):
    inp = -1
    while True:
        printHitMenu();
        inp = input();
        if inp == 1:
            #false if busted
            if hit(deck, player) == False:
                return False
        elif inp == 2:
            return True
        else:
            print("Not a valid entry")
 
def printHitMenu():
    print('1: Hit')
    print('2: Stay')   

def printMenu():
    print('1: New Game')
    print('2: Quit')
