rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random

user_choice = int(input("What do you choose? Type '0' for rock, '1' for paper, and '2' for scissors\n"))

comp_choice = random.randint(0, 2)

if user_choice == 0:
  print(rock)
elif user_choice == 1:
  print(paper)
else:
  print(scissors)

print("Computer chose")
if comp_choice == 0:
  print(rock)
elif comp_choice == 1:
  print(paper)
else:
  print(scissors)

# Now how to compare the choices and determine the winner
if user_choice == 0 and comp_choice == 0:
  print("You tied.")
elif user_choice == 0 and comp_choice == 1:
  print("You lose.")
elif user_choice == 0 and comp_choice == 2:
  print("You win.")
elif user_choice == 1 and comp_choice == 0:
  print("You win.")
elif user_choice == 1 and comp_choice == 1:
  print("You tied.")
elif user_choice == 1 and comp_choice == 2:
  print("You lose.")
elif user_choice == 2 and comp_choice == 0:
  print("You lose.")
elif user_choice == 2 and comp_choice == 1:
  print("You win.")
elif user_choice == 2 and comp_choice == 2:
  print("You tied.")