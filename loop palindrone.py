def pali(n):
    a=n
    rev=0
    while n>0:
        d=n%10
        rev=rev*10+d
        n=n//10
    if rev==a:
        return 1
    else:
        return 0
n=int(input("Enter a number "))
p=pali(n)
if p==1:
    print("palindrone")
else:
    print("not palindrone")
