#!/usr/bin/env python

# Task 13
#
# Rewrite the code shown below as a single line Ternary expression.
# if age >= 18:
# 	print("you are an adult")
# else:
# 	print("you are not an adult, yet!")

if __name__ == "__main__":
    age = int(input("Please enter your age: "))
    print("you are an adult" if age >= 18 else "you are not adult, yet")


# Output:
#
# Please enter your age: 23
# you are an adult
#
# Please enter your age: 16
# you are not adult, yet