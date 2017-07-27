

def calcmaxi(arra,numb):
    j = 0
    maxi = arra[j]
    while j < numb:
        if arra[j] > maxi:
            maxi = arra[j]
        j = j + 1
    print("max: ",maxi)

def calcmini(arra,numb):
    k = 0
    mini = arra[k]
    while k < numb:
        if arra[k] < mini:
            mini = arr[k]
        k = k + 1
    print("min: ",mini)



num = int(input("How many numbers do you want to enter?"))
arr = []
i = 0
while i < num:
    x = int(input("Enter your number:"))
    arr.append(x)
    i = i + 1


calcmaxi(arr,num)
calcmini(arr,num)