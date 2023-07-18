#Dice game 


import random
import time

dice_drawing = {
        0: (
            "-----",
            "|   |",
            "| o |",
            "|   |",
            "-----",
        ),
        1: (
            "-----",
            "|o  |",
            "|   |",
            "|  o|",
            "-----",
        ),
        2: (
            "-----",
            "|o  |",
            "| o |",
            "|  o|",
            "-----",
        ),
        3: (
            "-----",
            "|o o|",
            "|   |",
            "|o o|",
            "-----",
        ),
        4: (
            "-----",
            "|o o|",
            "| o |",
            "|o o|",
            "-----",
        ),
        5: (
            "-----",
            "|o o|",
            "|o o|",
            "|o o|",
            "-----",
        ),
    }
def displayImage():
    for x in range(6):
      print("\n".join(dice_drawing[x]),end="")
      print()
      time.sleep(0.2)
        

def roll():

    

    response =  input("The game is just for two person!: continue? (Yes/No) : ")
    if(response.lower() == "Yes".lower()):
        RollTime = int(input("How many times do you want to roll the dice? : "))
    
        firtPlayer = input("Enter first player name: ")
        firtPlayer_values = []
        print("Welcome "+ firtPlayer)
        
        print("rolling dics...")
        displayImage()
        for x in range(RollTime):
            randomDice = random.randint(1,6)
            firtPlayer_values.append(randomDice)
            
            
         
        secondPlayer = input("Enter second player name: ")
        secondPlayer_values = []
        print("Welcome "+ secondPlayer)
        
        print("rolling dics...")
        displayImage()
        for x in range(int(RollTime)):
        # Some loading animations here
            randomDice = random.randint(1,6)
            secondPlayer_values.append(randomDice)
        
        print("Calculating ...")
        
        total_for_player_1 = 0
        total_for_player_2 = 0
        
        # for firstplayer
        for x in firtPlayer_values:
            total_for_player_1 = total_for_player_1 + x
        for x in secondPlayer_values:
            total_for_player_2 = total_for_player_2 + x
            
        print(f"Total point for Player {firtPlayer}: {total_for_player_1} in the order: {firtPlayer_values}")
        print(f"Total point for Player {secondPlayer}: {total_for_player_2} in the order: {secondPlayer_values}")
        if(total_for_player_2 > total_for_player_1):
            print(f"{secondPlayer} won!")   
        elif(total_for_player_1>total_for_player_2):
            print(f"{firtPlayer} won!")
    else:
        print("Game Over")
        exit()
roll()

