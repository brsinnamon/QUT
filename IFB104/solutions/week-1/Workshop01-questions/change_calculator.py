# Change Calculator
#
# THE PROBLEM
#
# You need to calculate how much change is due when you go shopping.
# You have a $20 note and buy the following:
#   2 cartons of milk @ $2.50
#   5 Mars bars @ $1.20 each
#   1 pkt indigestion tablets @ $3.50
#
# Write an expression to calculate the change you should be given
# from $20, after buying those groceries.  Display the value of the
# change in a message to the screen.

# HINTS:
# * You will need to use built-in mathematical operators: *, + and -
# * You may like to introduce variables to accumulate and store values
# * The Python function call "print(E)" will print the value of expression E


### SOLUTION BELOW ###

# Declare the cost of individual items from the shop
carton_of_milk_price = 2.5
mars_bar_price = 1.2
pkt_indigestion_tablets_price = 3.5

# Calculate total cost of items purchased
milk_cost = carton_of_milk_price * 2
mars_bar_cost = mars_bar_price * 5 # not good for your health
pkt_indigestion_tablets_cost = pkt_indigestion_tablets_price * 1 # you're gonna need it

# Calculate total cost of all items
total_cost = milk_cost + mars_bar_cost + pkt_indigestion_tablets_cost

# Calculate change to give
dollar_note_given = 20.0
change = dollar_note_given - total_cost

# Display the value of the change in a message to the screen
print("Change owed to the customer:", change)

# Solution with an f string
print("Change should be $%.2f" % change)