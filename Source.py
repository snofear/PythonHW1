def moodChecker():
    mood = input("Please enter your current mood.\n")
    if mood=="happy":
        print("It is great to see you happy!\n")
    elif mood=="nervous":
        print("Take a deep breath 3 times.\n")
    elif mood=="sad":
        print("Talk to friends.\n")
    elif mood=="excited":
        print("It is great to be excited.\n")
    elif mood=="relaxed":
        print("Come with me to the party.\n")
    else:
        print("I don't recognize this mood.\n")


def secretNumber():
    secret = 6
    guess = -1
    jePrvi = True
    while(secret!=guess):
        if jePrvi==False:
            print("Your number is not correct.\n")
        else:
            jePrvi = False
        guess=int(input("Guess secret number. 0-10\n"))
    print("Your numer is correct!\n")


def calculator():
    number1 = int(input("Your first number?\n"))
    number2 = int(input("Your second number?\n"))
    operator = input("Which arithemtic operation do you want?\n")
    if operator=="+":
        print(number1+number2)
    elif operator=="-":
        print(number1-number2)
    elif operator=="*":
        print(number1*number2)
    elif operator=="/":
        print(number1/number2)
    else:
        print("Something went wrong...")
        

if __name__ == "__main__":
    moodChecker()
    secretNumber()
    calculator()
