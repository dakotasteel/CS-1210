"""
Number Guesser
Dakota Marosi
CS 1210
Program sees if a player can guess number between 1-1024
"""

import random        # Don't change this line!
import sys           # Don't change this line!

MAX_GUESSES = 10     # Don't change this line!
UPPER_BOUND = 1024   # Don't change this line!


def guess(target, guesses):
    running = True
    get_guess = int(input("Enter your guess: "))

    while running == True:
        if get_guess == target:
            running == False
            return True
        elif get_guess <= 0 or get_guess > 1025:
            print("INVALID! Guesses must be in the range [1, 1024]. Try again.")
            running == True
        elif get_guess in guesses:
            print(f"INVALID! You have already guessed {target}. Try again.")
            running == True
        else:
            guesses.append(get_guess)
            running == False
            return False


def play(target):
    """This function should take a secret number (target) and play the game.
    You'll need a list to hold the user's guesses, and then prompt the user to
    make guesses until they WIN! or they run out of guesses, in which case they
    LOSE! You should have a loop, and within the loop you should call the
    guess() function (above) as needed. It is in this function that you should
    report the number of guesses remaining, whether the current guess is HIGH!
    or LOW! (if not a WIN!), and the final outcome of the game: WIN! or
    LOSE! """
    guesses = []
    win = False

    for i in range(10):
        guess(target, guesses)
        
        if guesses[i] < target:
            print("Guess is too HIGH!")
        elif guesses[i] > target:
            print("Guess is too LOW!")

        
if __name__ == '__main__':
    if len(sys.argv) > 1:                # Don't change this line!
        random.seed(sys.argv[1])         # Don't change this line!
    print(f"Try to guess the secret number from 1 to {UPPER_BOUND}.")     
    secret_number = random.randint(1, 1025)
    play(secret_number)                  # Don't change this line!
    # No more lines are needed here!
