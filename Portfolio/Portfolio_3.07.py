#!/usr/bin/env python 3

# Task 7
#
# Modify your "Times Table" program so that the user enters the number of the table
# they require. This number should be between 0 and 12 inclusive.
if __name__ == "__main__":
    x = int(input("Please type a number between 0 and 12: "))
    for i in range(0,13):
        print(f"{i} x {x} = {i*x}")


# Output:
#
# Please type a number between 0 and 12: 4
# 0 x 4 = 0
# 1 x 4 = 4
# 2 x 4 = 8
# 3 x 4 = 12
# 4 x 4 = 16
# 5 x 4 = 20
# 6 x 4 = 24
# 7 x 4 = 28
# 8 x 4 = 32
# 9 x 4 = 36
# 10 x 4 = 40
# 11 x 4 = 44
# 12 x 4 = 48