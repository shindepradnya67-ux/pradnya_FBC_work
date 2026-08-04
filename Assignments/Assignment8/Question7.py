# WAP to find sum of digits of a number.
def sum_digit(n):
    sum=0
    while n>0:
        rem=n%10
        sum=sum+rem
        n=n//10
    return sum
num=int(input("Enter the n : "))
result=sum_digit(num)
print("Sum=",result)