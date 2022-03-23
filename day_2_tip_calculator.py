#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to the tip calculator!")
total_bill = input("What was the total bill?\n$")
tip_percentage = input("How much tip would you like to give? 10, 12, or 15?\n")
people = input("How many people to split the bill?\n")
total_as_float = float(total_bill)
tip_multiplier = 1 + int(tip_percentage)/100
shared_by = int(people)
per_person = round((total_as_float/shared_by)*tip_multiplier, 2)
final_amount = "{:.2f}". format(per_person)
print(f"Each person should pay: ${final_amount}")