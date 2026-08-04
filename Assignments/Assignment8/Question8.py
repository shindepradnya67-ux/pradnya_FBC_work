## WAP to find reverse number.
def reverse(n):
    rev=0
    while n>0:
        rem=n%10
        rev=rev*10+rem
        n=n//10
    return rev
num=int(input("Enter the number : "))
result=reverse(num)
print("Reverse=",result)