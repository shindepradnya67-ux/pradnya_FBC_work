## WAP to reverse a number using recursion 
def reverse (n,rev):
    if n==0:
        return rev
    else:
        rem=n%10
        rev=rev*10+rem
        return reverse(n//10 , rev)
num=int(input("Enter the number: "))
res=reverse(num,0)
print("Reverse = ",res)