#!usr/bin/env python 3

# Task 11

# Try writing an if statement similar to the last example that includes
# an extra elif clause to check ages between 30-40. Print a suitable message in the associated code block.
# if age > 100:
# 	print("you are very old,")
# 	print("well done!")
# elif age > 80:
# 	print("you are fairly old")
# print("pretty good!")
# elif age > 40:
# 	print("you are middle aged")
# print("never mind")
# else:
# 	print("you are not very old - yet")

if __name__ == "__main__":
    age = int(input("Please enter your age: "))
    if age > 100:
        print("you are very old,")
        print("well done!")
    elif age > 80:
        print("you are fairly old")
        print("pretty good!")
    elif age > 40:
        print("you are middle aged")
        print("never mind")
    elif 30 <= age <= 40:
        print("Congratulation! You are adult!")
        print("Hopefully!")
    else:
        print("you are not very old - yet")

# Output:
#
# Please enter your age: 30
# Congratulation! You are adult!
# Hopefully!
