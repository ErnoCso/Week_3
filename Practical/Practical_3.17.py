#!/usr/bin/env python 3

# Task 17
#
# Amend your previous solution so that if any value within the
# list is found to be over 100 then the loop should break immediately.


if __name__ == "__main__":
    numbers = [10, 20, 30, 90, 200, 30, 22, 11]
    order = ["1st", "2nd", "3rd", "4th", "5th", "6th", "7th", "8th"]
    running_total = 0
    breaker = 100
    for x, i in enumerate(numbers):
        if i > breaker:
            print(f"The next number ({i}) is greater than 100, so the loop stops")
            break
        else:
            print(f"{order[x]} number is {i} ==> {running_total} + {i} Running Total: {running_total+i}")
            running_total += i


# Output:
#
# 1st number is 10 ==> 0 + 10 Running Total: 10
# 2nd number is 20 ==> 10 + 20 Running Total: 30
# 3rd number is 30 ==> 30 + 30 Running Total: 60
# 4th number is 90 ==> 60 + 90 Running Total: 150
# The next number (200) is greater than 100, so the loop stops