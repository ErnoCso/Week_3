#!/usr/bin/env python 3

# Task 15
#
# Input and execute a for loop that uses a range() function to generate the following output:
# 2 to the power of 2 = 4
# 4 to the power of 4 = 256
# 6 to the power of 6 = 46656
# 8 to the power of 8 = 16777216
# 10 to the power of 10 = 10000000000

if __name__ == "__main__":
    for i in range(2, 11, 2):
        print(i, "to power of", i, " = ", i**i)

# Output:
#
# 2 to power of 2  =  4
# 4 to power of 4  =  256
# 6 to power of 6  =  46656
# 8 to power of 8  =  16777216
# 10 to power of 10  =  10000000000