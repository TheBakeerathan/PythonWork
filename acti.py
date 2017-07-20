def gettemp(temp):
    if temp > 60 and temp < 90:
        print("It is warm")
    elif temp >= 90:
        print("It is hot")
    elif temp < 60:
        print("It is chilly")

t = int(input("What is temperature?"))
gettemp(t)



