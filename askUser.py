def askuser():  # ask user if he/she leaves
    ask = input("Do you want to go(leave)?(Yes/No)")
    goloop(ask)


def goloop(ans):  # route and looping area
    if ans == "Yes" or ans == "yes":
        print("Good Bye! See you again!!")
    elif ans == "No" or ans == "no":
        askquest()
    else:
        print("Please say 'Yes' or 'No'")
        askuser()


def askquest():  # Question area
    name = input("What's your name?")
    print("Nice to meet you ", name)
    colour = input("What's your favourite colour?")
    print(colour, "? That's a nice colour")
    food = input("What's your favourite food?")
    print(food, "sounds yummy!")
    askuser()


goloop(ans="No")  # First time Pgm doesn't ask user if he/she leaves
