#!usr/bin/env python 3

# Task 12
#
# name = input("Enter your name: ")
# if name:
#  	print("Your name is", name)
# else:
#   print("Name not entered")
# Rewrite the above code that inputs a name then prints a message,
# but change the condition, so it explicitly uses a Boolean expression.
# Use the example below to help.
# if total != 0:
# 	print("Total is non-zero")
# else:
# print("Total is zero")

if __name__ == "__main__":
    name = input("Enter your name: ")
    if name == "":
        print("Dear Stranger!\nYou didn't enter anything! Are you a secret agent?")
    elif name == " ":
        print("Dear Stranger!\nYou didn't enter anything ! Are you a secret agent?")
    else:
        print(f"Your name is {name}! Hello {name}!")

# or another solution

    name = input("\nPlease enter your name: ")
    if name != "" or " ":
        print(f"Your name is {name}! Hello {name}!")
    else:
        print("Dear Stranger!\nYou didn't enter anything! Are you a secret agent?")


# Output:
#
# Enter your name:
# Dear Stranger!
# You didn't enter anything ! Are you a secret agent?name = input("\nPlease enter your name: ")
#     if name != "" or " ":
#         print(f"Your name is {name}! Hello {name}!")
#     else:
#         print("Dear Stranger!\nYou didn't enter anything! Are you a secret agent?")
#
# Please enter your name:
# Your name is  ! Hello  !
#
# Enter your name: Ernie
# Your name is Ernie! Hello Ernie!
#
# Please enter your name: Frankie
# Your name is Frankie! Hello Frankie!
