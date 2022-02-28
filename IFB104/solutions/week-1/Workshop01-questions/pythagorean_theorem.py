# Pythagorean Theorem
#
# THE PROBLEM
#
# Recall from high-school geometry lessons Pythagoras' famous
# theorem about right-angled triangles:
#
#   "The square of the hypotenuse equals the sum of the squares
#    of the other two sides"
#
# Write an expression to calculate the length of a right-angled
# triangle's hypotenuse given the lengths of the other two sides.
# For instance, given the two lengths below the answer should
# equal 5.
#
# COMMENT: This is not especially hard, but we're not going to
# give you any hints.  In particular, you will need to find out
# for yourself how to express the required mathematical formula
# in Python.  It's important that you know where to find such
# information by yourself because your Workshop Facilitators will
# not always be on hand to assist you.



side_a = 3
side_b = 4

### SOLUTION BELOW ###

from math import sqrt # this line should be at the top of the python code, but remains here with rest of my solution

def calculate_hypotenuse(opposite, adjacent):
    # Returns the length of a right-angled triangles' hypotenuse as a float given the lengths of the opposite and adjacent as arguments
    hypotenuse = sqrt((opposite ** 2) + (adjacent ** 2))
    return hypotenuse

print(f"Length of the hypotenuse is {round(calculate_hypotenuse(side_a, side_b),2)}")

print('\n')
print('----------------')


################################################################
#
# JUST FOR FUN
#
# In the classic MGM movie version of the "Wizard of Oz" we
# meet the Cowardly Lion who wants courage, the Tin Woodsman
# who wants a heart, the Scarecrow who wants a brain and, of
# course, young Dorothy who just wants to go home.  At the
# movie's end the Wizard gives the Scarecrow a diploma
# representing knowledge.  To demonstrate his new-found
# intelligence, the Scarecrow rapidly (mis)quotes the
# Pythagorean Theorem as follows:
#
#   "The sum of the square roots of any two sides of an
#    isosceles triangle is equal to the square root of the
#    remaining side"
#
# Ever since the movie was released in 1939 film historians
# have speculated about why the Scarecrow got the theorem
# so wrong.  (An isosceles triangle is one with two sides
# having the same length.  It's easy to show by counterexample
# that the Scarecrow's theorem is incorrect.  Try it.)
#
# Was this a simple blunder on the part of the scriptwriters?
# Or was it a subtle way of pointing out that the Scarecrow,
# although now happy, isn't any smarter than he was before?
# No one knows!  (You can find various copies of this scene
# on YouTube.)


### SOLUTION BELOW ###
# Some concerns with this code:
# 1. What should the height be set to? In this case it is selected randomly within a realistic range
# 2. Does this correctly test Scarecrow's theorem?

# use random to give an arbitrary height value of an isosceles triangle within a realistic range
from numpy import random

# Testing Scarecrow's theory for an isosceles triangle
# To disprove this theory we only need the length of one of the congruent sides and the height
# Select a random float for the length of the congruent side between 1 and 5
side_a = round(random.uniform(1, 5), 2)

# Declare an arbitrary height less than the length of the congruent legs of the isosceles triangle
height = round(random.uniform(0.1, side_a), 2)

def calculate_correct_base(leg, h):
    # Correctly calculate the third side (base) of the isosceles triangle for testing Scarecrow's theory
    result = 2 * (sqrt(leg ** 2) - sqrt(h ** 2))
    return result

def calculate_scarecrow_theory(leg, h):
    # leg is the length of the congruent sides
    # h is the height of the isosceles triangle
    # If we know the length of any two sides of an isosceles triangle, it follows that we know the length of one of the congruent sides (leg)
    
    # Calculate the length of the base according to Scarecrow's theory
    sum_square_roots_of_any_two_sides = sqrt(leg) * 2

    # Calculate the correct length of the base
    base = calculate_correct_base(leg, h)

    # Test if Scarecrow's theory matches established theorems
    if sum_square_roots_of_any_two_sides == sqrt(base):
        print("Scarecrow's theory is correct in this instance. But it is not yet proven.")
        return sum_square_roots_of_any_two_sides
    else:
        print("Scarecrow's theory is disproven.")
        return sum_square_roots_of_any_two_sides

print(f"Scarecrow's theory states that the length of the base is {round(calculate_scarecrow_theory(side_a, height),2)}, but instead it should be {round(calculate_correct_base(side_a, height),2)}")