i=0
while i<=200:
    j=1
    factors=0
    while j<=i:
        if i%j==0:
            factors=factors+1
        j=j+1
    if factors==2:
        print(i, " is a prime number")
    else:
        print(i, " is not a prime number")
    i=i+1