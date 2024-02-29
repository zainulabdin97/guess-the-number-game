#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

from art import logo
import random

print(logo)
print("Welcome to the Number Guessing Game!")
print("I am thinking of a number between 1 and 100.")

def easy():
  attempts = 10
  is_game_over = False
  number = random.randint(1, 100)
  print("You have 10 attempts remaining to guess the number.")

  while not is_game_over:
    
    if attempts == 0:
      print("You've run out of guesses, you lose.")
      break

    user_choice = int(input("Make a guess: "))
  
    if user_choice < number:
      print("Too low")
      attempts -= 1
      if attempts != 0:
        print("Guess again.")
        print(f"You have {attempts} attempts remaining to guess the number.")
      
    if user_choice > number:
      print("Too high")
      attempts -= 1
      if attempts != 0:
        print("Guess again.")
        print(f"You have {attempts} attempts remaining to guess the number.")
      
    if user_choice == number:
      print(f"You got it! The answer was {number}.")
      is_game_over = True

def hard():
  attempts = 5
  is_game_over = False
  number = random.randint(1, 100)
  print("You have 5 attempts remaining to guess the number.")

  while not is_game_over:

    if attempts == 0:
      print("You've run out of guesses, you lose.")
      break

    user_choice = int(input("Make a guess: "))

    if user_choice < number:
      print("Too low")
      attempts -= 1
      if attempts != 0:
        print("Guess again.")
        print(f"You have {attempts} attempts remaining to guess the number.")

    if user_choice > number:
      print("Too high")
      attempts -= 1
      if attempts != 0:
        print("Guess again.")
        print(f"You have {attempts} attempts remaining to guess the number.")

    if user_choice == number:
      print(f"You got it! The answer was {number}.")
      is_game_over = True

if input("Choose a difficulty level. Type 'easy' or 'hard': ") == "easy":
  easy()

else:
  hard()

