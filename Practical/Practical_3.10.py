#!usr/bin/env python 3

# Task 10

# Try writing an if statement that checks if someone is between the ages of 18 and 30 inclusive.
# If they are, then print a message saying "you are still young!"

if __name__ == "__main__":
    age = int(input("Please enter your age: "))
    if 18 < age <= 30:
        print("You are still young!")
    if 18 > age > 0:
        print("Your life is just beginning! Good luck!")
    if age == 0:
        print("Are you sure you entered the correct age? Because you weren't born then.")
    if age < 0:
        print("Impossible, unless you are a miracle!")
    if age > 30:
        print("You are mature!")

# Output:
#
# Please enter your age: 49
# You are mature!
#
# Please enter your age: 24
# You are still young!
#
# Please enter your age: -1
# Impossible!
#
# Please enter your age: 0
# Are you sure you entered the correct age? Because you weren't born then.