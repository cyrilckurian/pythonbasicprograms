def hcf(a,b):
     if(b==0):
         return a
     else:
          return hcf(b,a%b)
a=int(input("Enter a number"))
b=int(input("Enter second number"))
print("The gcd is:",end="")
print(hcf(a,b))
            
