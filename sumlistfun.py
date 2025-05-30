def calculate_sum(numbers):
    total=0
    for num in number:
        total+=num
        return total
    list=[]
n=int(input("enter the number of elementd in the list:"))
for i in range(n):
    num=eval(input("enter elements{}:".format(i+1)))
list.append(num)
result=calculate_sum(list)
print("sum of the list is",result)
    
 
