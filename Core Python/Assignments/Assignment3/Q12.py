## write a program to check if given 3 digit number is a palindrome or not.

## EX:121 is palindrome 

num= int(input('Enter the number three digit : '))
a=num//100
b=(num//10)%10
c=num%10

rev=c*100+b*10+a
if num == rev:
    print("The no is palindrome")
else :
    print("Not palindrome")