# Name generator

## Prompt the user for the kind of name they should generate

# dancer = 1
# film_star = 2
# star_wars = 3

# name_generator = input("What kind of name do you want to generate? ")

# dancer 
pet_name = input("What is your pet's name? ")
mom_name = input("What is your mom's maiden name? ")
print("Your Dancer Name is " + (pet_name + " " + mom_name))




# 1. Dancer
# 2. Film star
# 3. Star Wars

# Here are the formulas for each kind of name:

# Dancer:
# - Your first pet's name + your mother's maiden name

# Film star:
# - Your middle name + the street you grew up on


# Star Wars:
# - the Star Wars first name is the first three letters of their
#  real first name + the first two letters of their real last name.
# - the Star Wars last name is the first two letters of their 
# mother's maiden name + the first three letters of the city they were born in.

# Star Wars Hint: look up the "slice" syntax for python strings.

# ## For each kind of name, use input() to prompt them for each piece of information used to generate the name.

# # Bonus 1: After they generate a name, ask them if they would like to generate another 
# (and present them with the original choices).

# # Bonus 2: for each piece of information you ask them for, ask them "Is that correct?" 
# (Echoing back what they typed out)