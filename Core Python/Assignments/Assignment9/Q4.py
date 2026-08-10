## WAP to find sum of n numbers using recursion

def sum_num(n):
    if n==1:
        return 1
    else:
        return n+sum_num(n-1)
n=int(input("Enter the number : "))
res=sum_num(n)
print("sum=",res)