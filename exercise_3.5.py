def main():

    BAD_PASSWORDS = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']
    password = input("Please enter your password: ")
    if password in BAD_PASSWORDS:
        print("This is one of the forbidden words!\n Try it again!")
        main()
    elif len(password) < 8 or len(password) > 12:
        print("Please enter password between 8 and 12 ")
        main()
    else:
        password_again = input("Please reenter your password: ")
        if password == password_again:
            print("Password Set")
        else:
            print("The two password is doesn't match ")
main()