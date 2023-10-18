# accept input from user that saves their name in a variable
name = input("What's your name? ").strip().title()

"""
# see string functions here https://docs.python.org/3/library/stdtypes.html#stringmethods

# remove whitespace from beginningn and ed of string
name = name.strip()
# titlecase string
name = name.capitalize()
"""

# say Hello to user

""""
print parameters include 'sep' = seperator, 'end'.
Use \ to escape characters
"""
print("Hello,", name, end=". ")
print(name, "is great!", sep = "_")

# using 'f' allows you to insert variables using curly brackets
print(f"Your name is {name}")

