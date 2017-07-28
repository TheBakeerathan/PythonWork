import random
x=random.randint(1,10)

def correctness(num,gue):
    if num>gue:
        if(num-gue)==1:
            correct="Hot"
        elif(num-gue)==2:
            correct="Warm"
        else:
            correct="Cold"
    elif num==gue:
        correct="Amazing"
    else:
        if (gue - num) == 1:
            correct = "Hot"
        elif (gue - num) == 2:
            correct = "Warm"
        else:
            correct = "Cold"
    return correct


print("Welcome to the guessing game")
print("Here is your number (*)")

i=1
while i < 4:
    msg= "Attempt:"+ str(i) +" Please guess the number(1-10):"
    guess = int(input(msg))
    if guess==x:
        a=correctness(x,guess)
        print("Congrats! You guessed correctly. ",a)
    elif guess!=x and i<3:
        a = correctness(x, guess)
        print("Oops!! Here you got another chance ",a)
    else:
        print("Oooooops!! You lost the game")
    i=i+1