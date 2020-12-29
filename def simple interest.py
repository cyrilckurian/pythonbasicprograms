def simpleinterest(p,r,t):
    return((p*r*t)/100)
b=float(input("Enter principle amt "))
c=float(input("Enter time "))
d=float(input("Enter rate of interest "))
print("Simple interest is ",simpleinterest(b,c,d))
