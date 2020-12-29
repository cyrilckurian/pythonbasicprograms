#Simple stack program (manage employee data)
Employee=[]
c="y"
while(c=="y"):
    print("1.PUSH")
    print("2.POP")
    print("3.Display")
    choice=int(input("Enter your choice:"))
    if(choice==1):
        e_id=input("Enter employee no")
        ename=input("enter the employee name:")
        emp=(e_id,ename)
        Employee.append(emp)
    elif(choice==2):
        if(Employee==[]):
            print("stack empty")
        else:
            e_id,ename=Employee.pop()
            print("deleted element is:",e_id,ename)
    elif(choice==3):
        i=len(Employee)
        while i>0:
            print(Employee[i-1])
            i=i-1
    else:
        print("wrong choice")
        c=input("DO you want to continue or not?")

        
            
