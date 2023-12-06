print("#calculator")
x=int(input("enter your first number : "))
y=int(input("enter your second number : "))
print("what you want to do like\n for sum use = +\n for minus use = - \n for multyply use = *\n for division use = /\n for power use = **")
z=input("what you want : ")
# I TRYED with if and else you can use this with if & elif
if (z=='+') :
    print("your ans is : ",x+y)

elif (z=='-'):
    print("your ans is : ",x-y)

elif (z=='*'):
    print("your ans is : ",x*y)

elif(z=='/'):
    if y==0:
        print("division by 0 is not allowed !!!")
    else:
        print("your ans is : ",x/y)
        
elif(z=='**'):
    print("your ans is : ",x**y)

else:
    print("please select '+','-','*','/','**'")

print("donneeeee")