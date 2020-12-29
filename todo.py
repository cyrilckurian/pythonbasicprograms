s=[]
p=[]
c="y"
def add():
    a=input("Enter TO-DO :")
    s.append(a)
def delete():
    if(s==[]):
        print("stack to-do list")
    else:
        z=int(input("Which element to delete?"))
        print("Deleted element is: ",s.pop(z-1))
        print(" ")
def display():
    print("TO-DOs are as follows :")
    l=len(s)
    for i in range(0,l,1):
        print(s[i])
    print(" ")    
def mark():
    m=int(input("Which to-do is completed?"))
    m=m-1
    p.append(s[m])
    s.pop(m)
def displayc():
    print("TO-DOs COMPLETED")
    print(" ")
    u=len(p)
    for j in range(0,u,1):
        print(p[j])
    print(" ")
def stats():
    u=len(p)
    l=len(s)
    print("STATISTICS OF YOUR PROGRESS")
    print("TO-DOs INCOMPLETE",l )
    print("TO-DOs COMPLETED",u )
    sum= u + l
    pa= (u / sum )* 100
    pb = (l / sum ) * 100
    print("Percentage of incomplete TO-DOs",pb,"%")
    print("Percentage of completed TO-DOs",pa,"%")
    print(" ")
    
while(c=="y"):
    print("1.ADD")
    print("2.DELETE")
    print("3.DISPLAY")
    print("4.MARK to-do as completed")
    print("5.DISPLAY completed to-do")
    print("6.STATISTICS ")
    print("  ")
    choice=int(input("Enter your choice: "))
    print(" ")
    if(choice==1):
        add()
    elif(choice==2):
        delete()
    elif(choice==3):
        display()
    elif(choice==4):
        mark()
    elif(choice==5):
        displayc()
    elif(choice==6):
        stats()
    else:
        print("wrong input")
        c=input("Do you want to continue or not?")


    
        
    
