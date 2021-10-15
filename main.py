# Using this symbol I can leave comments that do not effect the code.
# Below this comment I will explain the various lines of code and their function within this file

# The import function is used to import modules from python to create specific functions for later use
# I will use both the array and random functions to create an 8 character password that is both random and strong

import random
import array

# Now I tell the interpater how long the password will be
# It will be 8 characters long
# However, it can be changed to any character length
MAX_LEN = 8

# Now I will create the indexes needed to pull data for my generator
Digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
Lower_case_characters = ['a', 'b', 'c', 'd', 'e', 'f',
                         'g', 'h', 'i', 'j', 'k', 'l',
                         'm', 'n', 'o', 'p', 'q', 'r',
                         's', 't', 'u', 'v', 'w', 'x',
                         'y', 'z']
Upper_case_characters = ['A', 'B', 'C', 'D', 'E', 'F',
                         'G', 'H', 'I', 'J', 'K', 'L',
                         'M', 'N', 'O', 'P', 'Q', 'R',
                         'S', 'T', 'U', 'V', 'W', 'X',
                         'Y', 'Z']
Special_characters = ['!', '@', '#', '$', '%', '^', '&', "*", '?', '/']

# My indexes are now created, future algorithms will now understand and reference these indexes for future use.
# Now I will combine my indexes so the program will have one centralized index to pull and randomize characters.

Combined_index = Digits + Lower_case_characters + Upper_case_characters + Special_characters

# Now I will tell the program to select at least one character from each list
rand_digit = random.choice(Digits)
rand_upper = random.choice(Upper_case_characters)
rand_lower = random.choice(Lower_case_characters)
rand_special = random.choice(Special_characters)

# This next line will create a temp password for future use in the combined index randomizer and array randomizer.

temp_pass = rand_digit + rand_upper + rand_lower + rand_special

# The next lines of code will now select random characters from the combined index
# the for x in range(MAX_LEN -4): will set apart 4 of the 8 characters to be randomized through the combined index
# created.


for x in range(MAX_LEN - 4):
    temp_pass = temp_pass + random.choice(Combined_index)

# and then plug those characters into an array for further randomization

    temp_pass_list = array.array('u', temp_pass)
    random.shuffle(temp_pass_list)

# Now I take the temp password from the array and then form it into a final password
# and print it.

password = ""
for x in temp_pass_list:
    password = password + x

print(password)

