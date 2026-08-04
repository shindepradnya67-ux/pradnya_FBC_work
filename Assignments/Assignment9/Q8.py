## WAP to check whether a number is prime or not using recursion
def prime(n,i):
    if i==1:
        return True
    elif n%i==0:
        return False
    else:
        return prime(n,i-1)
n=int(input("Enter the number: "))
if n<2:
    print("Not prime")
elif prime(n,n//2):
    print("prime number")
else:
    print("Not prime")