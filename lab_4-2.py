# Creator CS 10/8/2022


#First Variable
school = 'Fairfield Prep'

# Using .split First Half
first_half, second_half = school.split(' ')

# Or with slicing
first_half = school[:9]
second_half = school[9:]

# print the halves
print(first_half)
print(second_half)

# joined result
print(first_half + second_half)