number = int(input("Please type which time table you want to see :"))
if number < 0:
    for n in range(12, 0, -1):
        print(n, "*", number, "equals", n * number)
for n in range(1, 13):
    print(n, "*", number, "equals", n * number)