#!/usr/bin/env python
# coding: utf-8

# In[4]:


import random

#Some ascii arts for rock, paper, and scissors

#Rock ASCII art
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
#Paper ASCII art
paper = '''
    _______
---'   ____)____
          ______)
          _______)
        _______)
---.__________)
'''
#Scissors ASCII art
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
play_again = ("") #initializing the play_again variable, the variable type is empty string touple
games = 0
won = 0
lost = 0
draw = 0

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
            draw += 1
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
            draw += 1
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
            draw += 1
            games += 1
    
    play_again = ("")
    while play_again not in ("Y","y","N","n"):
        play_again = input("Play again? Y/N ")

if games == 1:
    print(f"You have played {games} game. You won {won} time, lost {lost} time, and draw {draw} time.")
else:
    if won == 1 and lost == 1 and draw == 1:
        print(f"You have played {games} games. You won {won} time, lost {lost} time, and draw {draw} time.")
    else:
        if won > 1 and lost == 1 and draw == 1:
            print(f"You have played {games} games. You won {won} times, lost {lost} time, and draw {draw} time.")
        elif won == 1 and lost > 1 and draw == 1:
            print(f"You have played {games} games. You won {won} time, lost {lost} times, and draw {draw} time.")
        elif lost == 1 and draw == 1 and won > 1:
            print(f"You have played {games} games. You won {won} time, lost {lost} time, and draw {draw} times.")
        elif won > 1 and lost > 1 and draw == 1:
            print(f"You have played {games} games. You won {won} times, lost {lost} times, and draw {draw} time.")
        elif won > 1 and lost == 1 and draw > 1:
            print(f"You have played {games} games. You won {won} times, lost {lost} time, and draw {draw} times.")
        elif won == 1 and lost > 1 and draw > 1:
            print(f"You have played {games} games. You won {won} time, lost {lost} times, and draw {draw} times.")
        elif won > 1 and lost > 1 and draw > 1:
            print(f"You have played {games} games. You won {won} times, lost {lost} times, and draw {draw} times.")
        elif won > 1 and lost <= 1 and draw <= 1:
            print(f"You have played {games} games. You won {won} times, lost {lost} time, and draw {draw} time.")
        elif won <= 1 and lost > 1 and draw <= 1:
            print(f"You have played {games} games. You won {won} time, lost {lost} times, and draw {draw} time.")
        elif won <= 1 and lost <= 1 and draw > 1:
            print(f"You have played {games} games. You won {won} time, lost {lost} time, and draw {draw} times.")


# In[ ]:





# In[ ]:




