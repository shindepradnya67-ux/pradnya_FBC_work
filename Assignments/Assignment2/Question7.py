## Find the sum of three-digit number 
##Program
num=int(input('Enter a three_digit number : '))
d1=num//100
d2=(num//10)%10
d3=num%10

sum=d1+d2+d3
print("sum of digits = ",sum)