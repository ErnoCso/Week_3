#!/usr/bin/env python 3

# Task 4
#
# Modify your program again so that the chosen password cannot be one of a list of
# common passwords, defined thus:
# BAD_PASSWORDS = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']

if __name__ == "__main__":
    while True:
        BAD_PASSWORDS = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']
        password = input("Please enter your password: ")
        if password in BAD_PASSWORDS:
            print("This is one of the forbidden words!")

        elif len(password) < 8 or len(password) > 12:
            print("Please enter password between 8 and 12 ")

        else:
            while True:
                password_again = input("Please reenter your password: ")
                if password == password_again:
                    print("Password Set")
                    exit()
                else:
                    print("Error! The two passwords do not match!")

# Output:
#
# Please enter your password: Ter
# Please enter password between 8 and 12
# Please enter your password: Tere
# Please enter password between 8 and 12
# Please enter your password: password
# This is one of the forbidden words!
# Please enter your password: letmein
# This is one of the forbidden words!
# Please enter your password: SantaClaus
# Please reenter your password: SantaCla
# Error! The two passwords do not match!
# Please reenter your password: SantaClaus
# Password Set