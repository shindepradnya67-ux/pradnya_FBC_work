## with parameter + with return
def fibonacci(n):
    a=-1
    b=1
    series=""
    for i in range(n):
        c=a+b
        series = series+str(c)+" "
        a=b
        b=c
    return series
num=int(input("Enter the number : "))
ans=fibonacci(num)
print(ans)
