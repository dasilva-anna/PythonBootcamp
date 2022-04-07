from replit import clear
#HINT: You can call clear() to clear the output in the console.
logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)

bids = {}

should_continue = True

def find_highest_bidder (bid_amounts):
  highest_bid = 0
  winner =""
  for bidder in bid_amounts:
    bid_amount = bid_amounts[bidder]
    if bid_amount > highest_bid:
      highest_bid = bid_amount
      winner = bidder
  print (f"The winner is {winner} with a bid of {highest_bid}")
    
while should_continue:
  name = input("What is your name? ")
  amount = int(input("What is your bid? $"))
  
  bids[name] = amount
  
  restart = input("Are there any other bidders? Type 'yes or 'no'. ").lower()
  
  if restart == "yes":
    clear()
    
  elif restart == "no":
    should_continue = False
    find_highest_bidder(bids)

