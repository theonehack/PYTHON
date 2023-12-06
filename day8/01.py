# gating factorial value


#lets make a function
def factorial (n):
    if (n==0 or n==1):
        return 1
    else:
        return n * factorial(n-1)


# def gerinput (c): 
    c=int(input("which number factorial you want .. "))


   
c=int(input("which number factorial you want .. "))
# print(gerinput)
print(factorial(c))


#lets run one more time 
