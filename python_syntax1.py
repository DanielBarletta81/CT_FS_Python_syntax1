# Task 1

weather = "sunny"

if weather == "sunny":
    print("Wear sunglasses!")
else:
    print("Take an umbrella!")


# Task 2 
    # Ask user how they feel today. 
#If they say "happy", 
#print "That's great to hear!",
 #and if they say "sad", 
#print "I hope your day gets better!".

mood = input("How do you feel today? ")

if mood == "happy":
    print("That's great to hear!") 
elif mood == "sad":
    print("I hope your day gets better!")
else:
    print("I do not understand that feeling.")

# Task 3

    # Original Code
""" mood = "excited"
 
if mood == "excited":
    print("Yay! Let's have fun.")
    else:
print("Let's find something fun to do!")
 """

# Corrected Indentation

mood = "excited"

if mood == "excited":
    print("Yay! Let's have fun.")
else:
    print("Let's find something fun to do!")

# Task 3.1 
#Grocery Store Math Calculate the total cost of three items you'd commonly find 
# in a grocery store, given their individual prices.

cost_granola = 20

cost_apples = 10

cost_ice_cream = 30

total_cost = cost_granola + cost_apples + cost_ice_cream

print(total_cost)


# Task 3.2
# Bank Interest If you have a savings account with a particular initial amount and a 
# fixed yearly interest rate, calculate the total amount in your account after a year. 

amount_in_bank = 1000

yearly_interest_rate = .03

interest_accrued = amount_in_bank * yearly_interest_rate 
amount_after_year = amount_in_bank + interest_accrued

print(f'Amount in bank after 1 year: {amount_after_year}')