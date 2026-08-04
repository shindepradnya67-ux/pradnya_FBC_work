## WAP to find sum of following series using recursive functions.
## 1!+2!+3!+4!....+n!
def factorial(n):
    if n>0:
        return n*factorial(n-1)
    else:
        return 1
def series(n):
    if n==1:
        return factorial(1)
    else:
        return factorial(n)+series(n-1)
n=int(input("Enter the number : "))
print("Sum=",series(n))