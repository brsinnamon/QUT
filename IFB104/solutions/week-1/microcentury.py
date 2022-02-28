# How long is a microcentury?

days_per_standard_year = 365 # assume it's not in a leap year

leap_days_per_century = 100 // 4

hours_per_day = 24

minutes_per_hour = 60

minutes_per_day = hours_per_day * minutes_per_hour

print("Minutes per day:", minutes_per_day)

minutes_per_year = days_per_standard_year * minutes_per_day

print("Minutes per year:", minutes_per_year)

minutes_per_century = (minutes_per_year * 100) + (leap_days_per_century * minutes_per_day)

print("Minutes per century:", minutes_per_century)

microcentury = minutes_per_century / 1000000

print("Microcentury is", round(microcentury), "minutes.")





