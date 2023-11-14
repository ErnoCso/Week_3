#!/usr/bin/env python 3

# Task 3
#
# Modify your previous program so that the password must be between 8 and 12
# characters (inclusive) long.

if __name__ == "__main__":
    while True:
        password = input("Please enter your password: ")
        if len(password) < 8 or len(password) > 12:
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
# Please enter your password: Holiday
# Please enter password between 8 and 12
# Please enter your password: SantaClaus
# Please reenter your password: SantaClau
# Error! The two passwords do not match!
# Please reenter your password: SantaClaus
# Password Set