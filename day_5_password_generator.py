#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
# combined_letter = random.sample(letters, nr_letters)
# combined_symbols = random.sample(symbols, nr_symbols)
# combined_numbers = random.sample(numbers, nr_numbers)
# password = ''.join(combined_letter) + ''.join(combined_symbols) + ''.join(combined_numbers)
# print(f"your password is {password}")

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
combined_letter = random.sample(letters, nr_letters)
combined_symbols = random.sample(symbols, nr_symbols)
combined_numbers = random.sample(numbers, nr_numbers)
length = nr_letters + nr_numbers + nr_symbols
pass_characters = combined_letter + combined_symbols + combined_numbers
password = ''.join(random.sample(pass_characters, len(pass_characters)))
print(f"Your password is {password}")