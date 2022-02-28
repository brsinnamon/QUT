# QUT Week 1 Activity:
# 6 - Earth vs Moon dry land area

# Quiz question from Time Magazine
# Which body has more dry land area? The Earth or the Moon?

from math import pi

# Calculate Earth's surface area measurements

earth_surface_area = round(5.1 * (10**8))  # Sq kilometres

print("Earth surface area:", earth_surface_area, "sq km.")

earth_water_area = round(earth_surface_area * 0.71) # 71% of Earth's surface area is water

print("Earth water area:", earth_water_area, "sq km.")

earth_land_area = round(earth_surface_area * (1 - 0.71)) # 100% - 71% is the Earth's land surface area

print("Earth land area:", earth_land_area, "sq km.")

# Calculate the Moon's surface area measurements

moon_diameter = 3475 #km

moon_radius = moon_diameter / 2

moon_surface_area = int(4 * pi * (moon_radius ** 2))

print("Moon's surface area:", moon_surface_area, "sq km.")

# Compare the two measurements to receive an answer.
# Which body's land area is larger? The Earth or the Moon's?

difference = earth_land_area - moon_surface_area

if (difference > 0):
    print("Earth's land area is larger than the Moon's by about", difference, "sq km.")

if (difference < 0):
    print("Moon's land area is larger than the Earth's by about", difference, "sq km.")