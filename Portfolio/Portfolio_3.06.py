#!/usr/bin/env python 3

# Task 6
#
# Write a program that displays the "Seven Times Table". That is, the result of
# multiplying 7 by every number from 0 to 12 inclusive. The output might start:
# 0 x 7 = 0
# 1 x 7 = 7
# 2 x 7 = 14
# and so on.

if __name__ == "__main__":
    for i in range(0,13):
        print(f"{i} x 7 = {i*7}")


# Output:
#
# 0 x 7 = 0
# 1 x 7 = 7
# 2 x 7 = 14
# 3 x 7 = 21
# 4 x 7 = 28
# 5 x 7 = 35
# 6 x 7 = 42
# 7 x 7 = 49
# 8 x 7 = 56
# 9 x 7 = 63
# 10 x 7 = 70
# 11 x 7 = 77
# 12 x 7 = 84