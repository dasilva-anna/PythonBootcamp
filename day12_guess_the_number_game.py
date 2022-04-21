import random
from replit import clear

logo = """
 __        __                       __                   __   __      
|    |  | |   |<< |<<   >>|<< |  | |     | | |  | |\ /| |  | |   |<<  
| >> |  | |<< --  --      |   |><| |<<   |\| |  | | < | |<>' |<< |>>| 
'__| '<<' |__ >>| >>|     |   |  | |__   | | '<<' |   | |__' |__ |  \ 

"""


# continue the game
should_continue = True

# easy mode function
def easy(num):
  attempts = 10
  while attempts != 0:
    print(f"You have {attempts} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    if guess == num:
      print(f"You got it! The answer was {num}.")
      attempts = 0
    elif guess > num:
      attempts -= 1
      print("Too high.")
      if attempts > 0:
        print("Guess again.")
      else:
        print("You've run out of guesses, you lose.")
    else:
      attempts -= 1
      print("Too low.")
      if attempts > 0:
        print("Guess again.")
      else:
        print("You've run out of guesses, you lose.")

# hard mode function
def hard(num):
  attempts = 5
  while attempts != 0:
    print(f"You have {attempts} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    if guess == num:
      print(f"You got it! The answer was {num}.")
      attempts = 0
    elif guess > num:
      attempts -= 1
      print("Too high.")
      if attempts > 0:
        print("Guess again.")
      else:
        print("You've run out of guesses, you lose.")
    else:
      attempts -= 1
      print("Too low.")
      if attempts > 0:
        print("Guess again.")
      else:
        print("You've run out of guesses, you lose.")

while should_continue:
  # Game introduction
  print(logo)
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100.")
  mode = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

  # Picking the number
  numbers = list(range(100))
  answer = random.choice(numbers)

  #Calling the functions
  if mode == "easy":
    easy(answer)
  elif mode == "hard":
    hard(answer)
  # Making sure there won't be errors
  else:
    print("invalid input")
    mode = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

  # Continue the game or not
  cont = input("Would you like to play again? Type 'y' or 'n': ").lower()
  if cont == 'y':
    clear()
  else:
    should_continue = False