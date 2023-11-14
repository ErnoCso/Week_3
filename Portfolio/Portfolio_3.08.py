#!/usr/bin/env python 3

# Task 8
#
# Modify the "Times Table" again so that the user still enters the number of the table,
# but if this number is negative the table is printed backwards. So entering "-7"
# would produce the Seven Times Table starting at "12 times" down to "0 times".

if __name__ == "__main__":
    x = int(input("Please type a number between -12 and 12: "))
    if x < 0:
        for i in range(12, -1, -1):
            print(f"{i} x {x} = {i*x}")
    if x >= 0:
        for i in range(0, 13):
            print(f"{i} x {x} = {i*x}")


# Output:
#
# Please type a number between 0 and 12: -5
# 12 x -5 = -60
# 11 x -5 = -55
# 10 x -5 = -50
# 9 x -5 = -45
# 8 x -5 = -40
# 7 x -5 = -35
# 6 x -5 = -30
# 5 x -5 = -25
# 4 x -5 = -20
# 3 x -5 = -15
# 2 x -5 = -10
# 1 x -5 = -5
# 0 x -5 = 0
#
# Please type a number between 0 and 12: 11
# 0 x 11 = 0
# 1 x 11 = 11
# 2 x 11 = 22
# 3 x 11 = 33
# 4 x 11 = 44
# 5 x 11 = 55
# 6 x 11 = 66
# 7 x 11 = 77
# 8 x 11 = 88
# 9 x 11 = 99
# 10 x 11 = 110
# 11 x 11 = 121
# 12 x 11 = 132