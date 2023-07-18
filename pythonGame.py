#Dice game 


import random

def roll():

    dice_drawing = {
        1: (
            "-----",
            "|   |",
            "| o |",
            "|   |",
            "-----",
        ),
        2: (
            "-----",
            "|o  |",
            "|   |",
            "|  o|",
            "-----",
        ),
        3: (
            "-----",
            "|o  |",
            "| o |",
            "|  o|",
            "-----",
        ),
        4: (
            "-----",
            "|o o|",
            "|   |",
            "|o o|",
            "-----",
        ),
        5: (
            "-----",
            "|o o|",
            "| o |",
            "|o o|",
            "-----",
        ),
        6: (
            "-----",
            "|o o|",
            "|o o|",
            "|o o|",
            "-----",
        ),

    }
    roll = input("Roll the dice? (Yes/No) : ")
    while roll.lower() == "Yes". lower():
        holdCorrect_value = 0
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        
        userGuess =    input("Guess the two numbers rolled (separated by space): ")
        split_UserGuess = userGuess.split(" ")
        
        if int(split_UserGuess[0]) == dice1 or int(split_UserGuess[1]) == dice1:
            holdCorrect_value = holdCorrect_value + 1
            
        if int(split_UserGuess[0]) == dice2 or int(split_UserGuess[1]) == dice2:    
            holdCorrect_value = holdCorrect_value + 1
        
        print("\n".join(dice_drawing[dice1]))
        print("\n".join(dice_drawing[dice2]))
        print("dice rolled: {} and {}". format(dice1, dice2))
        print("you guessed: {} and {}". format(split_UserGuess[0],split_UserGuess[1]))
        
        print("you got {} correct out of 2". format(holdCorrect_value))
        
        
        roll = input("Roll again? (Yes/no): ")
roll()

