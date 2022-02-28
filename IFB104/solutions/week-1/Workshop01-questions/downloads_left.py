# Music download credits
#
# THE PROBLEM
#
# Assume the following values have already been entered into the
# Python interpreter, denoting the cost in cents for downloading one
# music track, your original budget in dollars, and the number of tracks
# already downloaded:

from math import floor


track_cost = 120 # cost in cents for downloading one track
budget = 50 # dollars
num_downloaded = 15 # number of tracks already downloaded

# Write expressions to calculate how many more tracks you can afford
# to download and print that value to the screen.
#
# A problem solving strategy:
# 1. Calculate the amount spent so far by
#    multiplying the number downloaded by the track cost
# 2. Calculate the balance left by
#    deducting the amount spent so far from the budget
# 3. Divide the balance left by the track cost to a whole number
# 4. Print the number of tracks left
#
# Be careful to allow for the fact that one of the given values
# is expressed in cents and the other is in dollars, i.e., the
# units associated with the values are different.


### SOLUTION BELOW ###

# Calculate the amount spent so far
amount_spent = track_cost * num_downloaded

# Calculate the balance left so far
balance_remaining = (budget * 100) - amount_spent  # converted the budget variable from dollars to cents

# Credits remaining
credits_remaining = balance_remaining / track_cost

# Display the amount of music download credits remaining in a message to the screen
print(f"Number of track credits remaining: {floor(credits_remaining)}") # floor rounds down as there isn't enough credit to buy another track with remainder