## write a program to check if given 3 digit number is a palindrome or not.

num = int(input("Enter a 3-digit number : "))

a=num//100
b=(num//10)%10
c=num % 10

rev = c*100 + b*10 +a

if num == rev:
    print("Palindrome Number")
else :
    print("Not Palindrome ")

## EX:121 is palindrome 