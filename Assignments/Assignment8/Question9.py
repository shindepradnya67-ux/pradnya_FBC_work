## WAP to check entered number is palindrome or not
def palindrome(n):
    temp=n
    rev=0

    while n>0:
        rem=n%10
        rev=rev*10+rem
        n=n//10
    if temp==rev:
        return "palindrome Number"
    else:
        return "Not palindrome Number"
num=int(input("Enter the number : "))
ans=palindrome(num)
print(ans)