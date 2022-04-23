# Import packages and lists
from replit import clear
import random
import art
from game_data import data

# continue variable
should_continue = True

print(art.logo)

score = 0

while should_continue:
  a = random.choice(data)
  followers_a = a["follower_count"]
  print(f"Compare A: {a['name']}, a {a['description']}, from {a['country']}")

  print(art.vs)

  b = random.choice(data)
  followers_b = b["follower_count"]
  print(f"Against B: {b['name']}, a {b['description']}, from {b['country']}\n")  

  choice = input("Who has the most followers? Type 'A' or 'B' ").upper()

  if followers_a > followers_b:
    most_followers = 'A'
  elif followers_b > followers_a:
    most_followers = 'B'
  else:
    most_followers = 'tie'

  if most_followers == 'tie':
    print("They both have the same amount of followers")
    clear()
    print(art.logo)
    print(f"Current score: {score}")
  else:
    if choice == most_followers:
      score += 1
      clear()
      print(art.logo)
      print(f"You're right! Current score: {score}")
    else:
      should_continue = False
      print(f"Sorry, that's wrong. Final score: {score}")
  
  