## WAP to find sum of digits using recursion
def sum_digit(n):
    if n==0:
        return 0
    else:
        rem=n%10
        return rem+sum_digit(n//10)
n=int(input("Enter the number: "))
res=sum_digit(n)
print("sum of digits=",res)
