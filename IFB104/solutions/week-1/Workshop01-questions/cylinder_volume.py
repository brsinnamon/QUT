# Volume of a cylinder
#
# THE PROBLEM
#
# Assume the following values have already been entered into the
# Python interpreter, denoting the measurements of a cylindrical
# tank:

radius = 4 # metres
height = 10 # metres

# Also assume that we have imported the existential constant "pi"
# from the "math" library module:

from math import pi

# Write an expression, or expressions, to calculate the volume
# of the tank.  Print the result in a message to the screen.  (If
# you've forgotten the formula for the area of a circle and hence
# volume of a cylinder, ask one of your workshop partners!)

### SOLUTION BELOW ###

# Calculate the volume
volume = (pi * (radius ** 2)) * height

# Display the result of the calculation in a message to the screen
print(f"The volume of this cylinder with radius {radius}m and height {height}m is {round(volume,2)} cubic metres.")