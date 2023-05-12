
# For this week, we are going to make an interactive guessing game in Python.
# This is going to be a simple guessing game where the computer will generate a random number between 1 to 100,
# and the user has to guess it in 9 attempts.
# Based on the user's guess, the  computer will give various hints if the number is high or low. ' \
#                  'When the user guess matches the number computer will print the answer along with ' \
#                  'the number of attempts. You have to make the submission by uploading your github link to your ' \
#                  'repositories where you must have pushed your codes.

import random

computer_chose = random.randint(1, 10)
print(f" computer Number is: {computer_chose}")
is_game = True
number_attempts = 0

user_name = input("What is your Name? ").lower()
print(f"WELCOME TO TINKO GUESSING GAME NUMBER! {user_name} ")

while is_game:
    user_guess = int(input(f"{user_name.upper()} am thinking of a number between 1 To 100 .Can you make a guess "
                           f"you have 9 attempts "))

    if user_guess > computer_chose:
        number_attempts += 1
        print(f"{user_name.upper()} That is Too High for your {number_attempts} attempts ")
        if number_attempts == 9:
            is_game = False
        print(f"Sorry GAME OVER {user_name.upper()} you couldn't guess the number withing 9 "
              f"attempts but the Number is {computer_chose}")
    elif user_guess < computer_chose:
        print(f"{user_name.upper()} That is Too Low for your {number_attempts} attempts ")
        if number_attempts == 9:
            is_game = False
        print(f"Sorry GAME OVER {user_name.upper()} you couldn't guess the number withing 9 "
              f"attempts but the Number is {computer_chose}")
    elif user_guess == computer_chose:
        print(f"{user_name.upper()} Correct that is the Computer guessing Number {computer_chose} ")
        is_game = False

