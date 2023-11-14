#!/usr/bin/env python 3

# Task 18
#
# Amend your previous solution once again, so that the message “all numbers processed”
# is printed when the loop completes, but only if all values were less or equal to 100
# (i.e. the loop did not break early)


if __name__ == "__main__":

    numbers = [10, 20, 30, 90, 200, 30, 22, 11]
    order = ["1st", "2nd", "3rd", "4th", "5th", "6th", "7th", "8th"]
    running_total = 0
    breaker = int(input("Please choose a value above which the listing breaks. "
                        "\nPossible choices [10, 20, 30, 90, 200, 30, 22, 11]: "))
    print()
    list_total = True
    for x, i in enumerate(numbers):
        if i > breaker:
            list_total = False
            break
        else:
            print(f"{order[x]} number is {i} ==> {running_total} + {i} Running Total: {running_total+i}")
            running_total += i
    if list_total:
        print("All numbers processed")

# Output:
#
# Possible choices [10, 20, 30, 90, 200, 30, 22, 11]: 200
#
# 1st number is 10 ==> 0 + 10 Running Total: 10
# 2nd number is 20 ==> 10 + 20 Running Total: 30
# 3rd number is 30 ==> 30 + 30 Running Total: 60
# 4th number is 90 ==> 60 + 90 Running Total: 150
# 5th number is 200 ==> 150 + 200 Running Total: 350
# 6th number is 30 ==> 350 + 30 Running Total: 380
# 7th number is 22 ==> 380 + 22 Running Total: 402
# 8th number is 11 ==> 402 + 11 Running Total: 413
# All numbers processed
#
# Possible choices [10, 20, 30, 90, 200, 30, 22, 11]: 100
#
# 1st number is 10 ==> 0 + 10 Running Total: 10
# 2nd number is 20 ==> 10 + 20 Running Total: 30
# 3rd number is 30 ==> 30 + 30 Running Total: 60
# 4th number is 90 ==> 60 + 90 Running Total: 150