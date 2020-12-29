def sumOfList(list,size):
    if(size==0):
        return 0
    else:
        return list[size-1]+sumOfList(list,size-1)
list=[]
n=int(input("How many numbers"))
for i in range(n):
    num=int(input("Enter a number"))
    list.append(num)
total=sumOfList(list,len(list))
print("Sum of all elements in given list:",total)
