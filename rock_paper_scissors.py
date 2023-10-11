"""
CS 1210
Lab #7
Dakota Marosi
October 11th, 2023
"""
import random

      #  human
      # r  p   s  
RPS = [[0, 1, -1], # r
       [-1, 0, 1], # p   computer
       [1, -1, 0]] # s
LABELS = ['rock', 'paper', 'scissors']

if __name__ == "__main__":
    running = True
    while running == True:
        choice = int(input("What's your choice? 0) rock, 1) paper, 2) scissors? or 4) quit "))
        if choice == 4:
            print("Goodbye!")
            running = False
        else:
            computer_choice = random.randint(0,2)
            print(f"You: {LABELS[choice]} Me: {LABELS[computer_choice]}")
            win_or_lose = RPS[computer_choice][choice]

            if win_or_lose == 1:
                print("You win!")
            elif win_or_lose == 0:
                print("We tie!")
            else:
                print("I win!")
