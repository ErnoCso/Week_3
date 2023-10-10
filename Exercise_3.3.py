password = input("Please enter your password: ")
if len(password) < 8 or len(password) > 12:
    print("Please enter password between 8 and 12 ")
    exit()
else:
    password_again = input("Please reenter your password: ")
    if password == password_again:
        print("Password Set")
    else:
        print("Error. ")