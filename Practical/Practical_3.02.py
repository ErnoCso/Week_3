#!usr/bin/env python3

# Task 2

# Input a program that defines a variable called ‘age’ that is initialised to your own age.
# Then type several boolean expressions that compare the variable to see whether it is less than ‘18’, ‘21’ then ‘31’.
# Boolean expressions do not have to compare just numeric type values, they can also be used to compare other types.


age = int(input("Please type in your age: "))
if 18 >= age > 0:
    print("At your age, your mind is still as sharp as a razor, but if not, that won't change later either.")
elif 18 < age <= 20:
    print("you are older than 18, but not older than 21.")
elif 21 < age <= 30:
    print("you are older than 21 but not older than 31.")
elif 31 <= age < 50:
    print("you are older than 31, but not older than 50.")
elif 50 <= age < 122:
    print("Your age shows that you are too old, go and lie down for a while!")
else:
    print("Either you entered the wrong number, or you were never born, or you are the oldest person in history!")

# Output:

# Please type in your age: 49
# you are older than 31, but not older than 50.

# Please type in your age: 123
# Either you entered the wrong number, or you were never born, or you are the oldest person in history!
