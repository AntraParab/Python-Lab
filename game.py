#rock paper scissor game

import random

while True:
    choice=["rock","paper","scissor"]
    computer = random.choice(choice)
    player=None

    while player not in choice:
        player = input("rock paper or scissors??").lower()

    if player==computer:  
        print("computer-",computer)
        print("Player",player)
        print("Tie!")
    elif player=="rock":
        if computer=="scissor":
            print("computer-",computer)
            print("Player",player)
            print("you win!")
        if computer=="paper":
            print("computer-",computer)
            print("Player",player)
            print("you lose!")
    elif player=="paper":
        if computer=="scissor":
            print("computer-",computer)
            print("Player",player)
            print("you lose!")
        if computer=="rock":
            print("computer-",computer)
            print("Player",player)
            print("you win!")
    elif player=="scissors":
        if computer=="paper":
            print("computer-",computer)
            print("Player",player)
            print("you win!")
        if computer=="rock":
            print("computer-",computer)
            print("Player",player)
            print("you lose!")
    play_again=input("do you want to play further- (YES/NO)").lower()
    if play_again !="yes":
        break
print("bye")



     
    