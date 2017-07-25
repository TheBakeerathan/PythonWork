def ftoc(f):
    c =(f-32)*100/180
    print(f, "degree F equals to ", c, "degree C")
    looping()


def looping():
    ans =input("Do you want to continue? Say(Yes/No)")
    if ans == "Yes" or ans == "yes":
        asktemp()
    elif ans == "No" or ans == "no":
        print("Good Bye! See you Again")
    else:
        print("Please Say 'Yes' or 'No' ")
        looping()


def asktemp():
    ftemp = input("Please enter temperature in  F:")
    if ftemp.isnumeric() == True: # Checks if ftemp is number
        ftoc(int(ftemp))
    else:
        print("Please Enter only Numbers")
        asktemp()

asktemp()