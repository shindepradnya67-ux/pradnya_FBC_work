## WAP to find print the following fibonacci series using functions:
## without parameter + without return
def fibonacci():
    n=int(input("Enter the number : "))
    a=-1
    b=1
    for i in range(n):
        c=a+b
        print(c,end=" ")
        a=b
        b=c
fibonacci()