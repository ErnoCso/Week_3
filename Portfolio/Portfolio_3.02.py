#!/usr/bin/env python 3

# Task 2
#
# Write a program that simulates the way in which a user might choose a password.
# The program should prompt for a new password, and then prompt again.
# If the two passwords entered are the same the program should say "Password Set"
# or similar, otherwise it should report an error.

password_1 = input("Please enter a password: ")
password_2 = input("Please enter a password again: ")
if password_1 == password_2:
    print("Password Set")
else:
    print("Error! The two passwords do not match!")

# Output:
#
# Please enter a password: Something
# Please enter a password again: Something
# Password Set
#
# Please enter a password: S0MetHing
# Please enter a password again: S0metHing
# Error! The two passwords do not match!