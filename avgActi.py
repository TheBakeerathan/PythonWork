many=int(input("How many numbers do you have to get AVG?"))
sum =0
for a in range (1,many+1):
   print (" Enter Num ",a," :")
   sum = sum+int(input())
print("Your Sum is ",sum)
print("Your Average is ", sum/int(many))