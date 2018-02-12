#Save your life in jungle by using import random and import time
#usage of loops
#usgae of functions at basic level
import random
import time

def displayIntro():
    print('You are in the jungle.\n\nYou can see Dragons in front of you.')
    print("There is two dragons and two caves.\n\nIn one cave dragon is friendly\n and will share his cave with you.\n\n")
    print("The other dragon is hungry and\n will eat you on the sight.")
    print()

def chooseCave():
    cave = ''
    while cave != "1" and cave != "2":
        print('Which cave you will go? as you are having 2 cave options.(1 or 2)')
        cave = input()
    return cave

def checkCave(chosenCave):
    print("You reached the cave...")
    time.sleep(6)
    print("Its very dark cave...")
    time.sleep(5)
    print('The hungry dragon jumps on front of you.\nHe opens his mouth...')
    print()
    time.sleep(7)

    friendlyCave = random.randint(1,2)
    if chosenCave == str(friendlyCave):
        print("He will share with you.")
    else:
        print("He will eat you in one bite.")
playAgain = 'yes'
while playAgain == "yes" or playAgain == "y":

    displayIntro()
    caveNumber = chooseCave()
    checkCave(caveNumber)
    print("Do you want to play again? (Yes or No)")
    playAgain = input()




