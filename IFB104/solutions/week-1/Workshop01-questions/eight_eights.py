#--------------------
# Eight Eights
#
# Here's a challenging little puzzle you can solve with the
# help of Python.  Can you devise a numeric expression in
# which the digit 8 appears exactly 8 times and which
# evaluates to 1000?  To check your answer, evaluate the
# expression in Python and print the result.  There are many
# different solutions to this problem, so see if the other
# groups in your class come up with different answers.


#--------------------
# Integer version: Solve the problem using only the digit 8
# and the integer arithmetic operators +, -, * and //.  (You
# don't have to use them all.)  The result should be the
# integer value 1000.

##### Put the code to evaluate and print your expression here

### SOLUTION BELOW ###

### CHALLENGE ONE: INTEGER VERSION ###

# Define our operators for use
operators = ['+', '-', '*', '//']

formula = ''

length = len(operators)

lower, upper = 900, 1100

# Make a function which finds possible formulas that gives answers close to 1000
def find_the_formula():
    found_possible_formula = False
    for i in range(length):
        for j in range(length):
            for k in range(length):
                for l in range(length):
                    for m in range(length):
                        for n in range(length):
                            for o in range(length):
                                formula_string = f'{8} {operators[i]} {8} {operators[j]} {8} {operators[k]} {8} {operators[l]} {8} {operators[m]} {8} {operators[n]} {8} {operators[o]} {8}'
                                formula = eval(f'{8} {operators[i]} {8} {operators[j]} {8} {operators[k]} {8} {operators[l]} {8} {operators[m]} {8} {operators[n]} {8} {operators[o]} {8}')
                                if formula > lower and formula < upper:
                                    found_possible_formula = True
                                    print(f"Resultant: \n {formula_string} = {formula}")
    if found_possible_formula == False:
        print(f"No formulas found with answer within range {lower}-{upper}")

# This commented function below does not find the correct answer as it is unable to include the use of brackets to control the formula
# find_the_formula()

# After thinking about how I can create other numbers using just 8, I found an answer
# For example, to make 1 = (8/8), to make 2 = ((8+8)/8), to make 10 = ((8*8)/8)
int_eight = 8
int_three = ((8+8+8)/8)
int_sixteen = 8 + 8

trial_and_error_result = (((8+8) * 8) - ((8+8+8)//8)) * 8


trial_and_error_result_string = '(((8+8) * 8) - ((8+8+8)//8)) * 8'

print(f"Using integer arithmetic: \n {trial_and_error_result_string} = {trial_and_error_result}")



#--------------------
# Floating point version: Solve the problem using only the
# digit 8, decimal points, floating point arithmetic (+, -,
# * and /), the square root function and the exponentiation
# operator **.  (Again you don't have to use them all.)  In
# this case the result should be the floating point
# value 1000.0, but remember that the rounding errors inherent
# in computer arithmetic might not produce a mathematically
# precise result!

from math import sqrt
##### Put the code to evaluate and print your expression here
# Simply re-use my formula as it results in a float

float_eight = 8.0
float_three = ((8.0+8.0+8.0)/8.0)
float_sixteen = 8.0 + 8.0

floating_point_result = ((float_sixteen * float_eight) - float_three) * float_eight

print(f"Using floating point arithmetic results in: \n {floating_point_result}")