#!/usr/bin/env python 3

# Task 8

# Within the answer box below writes a small Python program that asks the user to enter two values.
# Store these values in two variables then output a message displaying the result of dividing
# the first value by the second value. Include code that prevents a run-time error being reported
# when the user inputs a value of '0' for the second input. Hint: use an ‘if’ statement
# If a '0' value is input, print a message saying, "division by 0 is not possible".

if __name__ == "__main__":
    while True:
        x = float(input("Please enter first value: "))
        y = float(input("Please enter second value: "))

        if x == 0 or y == 0:
            print("division by 0 is not possible")

        else:
            res = (x / y)
            print(f" {x} / {y} = {round(res,2)}")
            break

# Output:
#
# Please enter first value: 12
# Please enter second value: 23
#  12.0 / 23.0 = 0.52