#!/usr/bin/env python
# coding: utf-8

# In[103]:


import random

#Some ascii arts for rock, paper, and scissors

#0
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
#1
paper = '''
    _______
---'   ____)____
          ______)
          _______)
        _______)
---.__________)
'''
#2
scissors = '''
    _______
---'   ____)____
          ______)
        _________)
       (_____)
---.___(___)
'''

#-------------------------------------------
print("Welcome to the Classic \"Rock, Paper, Scissors\" Game!")
play_again = ("") #initializing the play_again variable
games = 0
won = 0
lost = 0

while play_again not in ("N", "n"):
    #Let the player choose first:
    player_choose = "" #initializing the player_choose variable

    while player_choose not in ("0", "1", "2"):
        player_choose = input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors.")

    #Player result conditions
    player_result = "" #initializing the player_result variable
    
    if player_choose == "0":
        player_result = rock
    elif player_choose == "1":
        player_result = paper
    else:
        player_result = scissors

    #Now, it's the computer's turn to choose
    computer_choose = random.randint(0,2)

    #Computer result conditions
    computer_result = "" #initializing computer_choose variable
    
    if computer_choose == 0:
        computer_result = rock
    elif computer_choose == 1:
        computer_result = paper
    else:
        computer_result = scissors

    #Show the results from both sides------------------------
    print(player_result)
    print("Computer chooses:")
    print(computer_result)

    #Let the game begin!-------------------------------------
    if player_result == rock:
        if computer_result == rock:
            print("It's a draw!")
            won += 0
            lost += 0
            games += 1
        elif computer_result == paper:
            print("Computer wins!")
            lost += 1
            games += 1
        else:
            print("You win!")
            won += 1
            games += 1

    if player_result == paper:
        if computer_result == rock:
            print("You win!")
            won += 1
            games += 1
        elif computer_result == paper:
            print("It's a draw!")
            won += 0
            lost += 0
            games += 1
        else:
            print("Computer wins!")
            lost += 1
            games += 1

    if player_result == scissors:
        if computer_result == rock:
            print("Computer wins!")
            lost += 1
            games += 1
        elif computer_result == paper:
            print("You win!")
            won += 1
            games += 1
        else:
            print("It's a draw!")
            won += 0
            lost += 0
            games += 1
        
    play_again = ("")
    while play_again not in ("Y","y","N","n"):
        play_again = input("Play again? Y/N ")

if games <= 1:
    print(f"You have played {games} game. You won {won} time, and lost {lost} time.")
else:
    if won <= 1:
        print(f"You have played {games} games. You won {won} time, and lost {lost} times.")
    
    if lost <= 1:
        print(f"You have played {games} games. You won {won} times, and lost {lost} time.")


# In[ ]:




