def calculategmean (a,b):
    x = (a*b)/(a+b)
    print(x)


def greternum (a,b):
    if(a>b):
        print("a is greter than b ")
    else:
        print("b is greter  or equal  ")
# for first one calculastion 
a=int(input("enter your first number : "))
b=int(input("enter your second number : "))
greternum(a,b)
calculategmean(a,b)

# for second one 

c=int(input("enter your first number : "))
d=int(input("enter your second number : "))
greternum(c,d)
calculategmean(c,d)