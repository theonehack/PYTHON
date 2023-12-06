#fibonachisequence
def fibo (n):
    if n==1:
        return 1
    if n==0:
        return 0
    else:
        for j in range(n):
            x=(j-1)+(j-2)
            print("f",j,"=",x)

print(fibo(int(input("what is your range of fibonachi series .. "))))

