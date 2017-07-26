def ctof(c):
    f=((180*c)/100)+32
    print(c, "degree C equals to......... ", f, "degree F")


temp=0
while temp <=100:
    ctof(temp)
    temp+=5