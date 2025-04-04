s=input("enter the list of numbers seperated by spaces")
s=list(map(int,s.split()))
sum=0
for sum in s:
    sum+=sum
    print("the sum of the number is:",sum)
