#!/usr/bin/env python 3

# Task 7
#
# Within the answer box below write a small Python program, that asks the user to enter a value between 1 and 10.
# Once the value has been input display a message saying whether the value was in the requested range.
# Remember: values returned from the input() function are strings, and need converting before being used
# within expressions, i.e., you will need code such as this -
# num = input("please enter a number between 1 and 10 : ")
# num = int(num)


def main():
    yes = ["Yes", "yes", "YES", "Y", "y", "Yeah", "yeah", "YEAH"]
    no = ["No", "no", "NO", "N", "n", "Nope", "nope", "NOPE"]
    x = float(input("Please enter a x value: "))
    y = float(input("Please enter a y value: "))
    print(f"The value 'y' is larger than the value 'x'" if x <= y else "The value 'x' is larger than the value 'y'")
    decision = input("\nWould you like enter an other number? Y/N\n")
    if decision in yes:
        main()
    elif decision in no:
        print("See you soon!")
        exit()
    else:
        print("Please enter valid data")
        main()


main()


# Output:
#
# Please enter a x value: 4
# Please enter a y value: 12
# The value 'y' is larger than the value 'x'
#
# Would you like enter an other number? Y/N
# y
# Please enter a x value: 45
# Please enter a y value: 23
# The value 'x' is larger than the value 'y'
#
# Would you like enter an other number? Y/N
# n
# See you soon!