# 10.  Write a Python program to check the validity of a password given by the user.

#The Password should satisfy the following criteria:
#1.  Contains at least one letter between a and z
#2.  Contains at least one number between 0 and 9
#3.  Contains at least one letter between A and Z
#4.  Contains at least one special character from $,  # , @
#5. Minimum length of password: 8

# Write a Python program to check the validity of a password given by the user.
password = input("Enter your password: ")

contains_lower = False
contains_upper = False
contains_number = False
contains_special = False
if len(password) >= 8:
    for char in password:
        if char.islower():
            contains_lower = True
        elif char.isupper():
            contains_upper = True
        elif char.isnumeric():
            contains_number = True
        elif char in ['$', '#', '@']:
            contains_special = True

    if contains_lower and contains_upper and contains_number and contains_special:
        print("Password is valid.")
    else:
        print("Password is invalid.")
else:
    print("Password is too short.")
