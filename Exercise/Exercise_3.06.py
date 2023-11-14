#!/usr/bin/env python 3

# Task 6
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
    x = int(input("Please enter a number between 1 and 10: "))
    print(f"The number between 1 and 10" if x <= 10 else "You little cheater, it's not between one and ten")
    decision = input("Would you like enter another number? Y/N")
    if decision in yes:
        main()
    elif decision in no:
        print("See you soon!")
        exit()


main()

# Output:
#
# Please enter a number between 1 and 10: 6
# The number between 1 and 10
# Would you like enter another number? Y/Ny
# Please enter a number between 1 and 10: 11
# You little cheater, it's not between one and ten
# Would you like enter another number? Y/Nn
# See you soon!