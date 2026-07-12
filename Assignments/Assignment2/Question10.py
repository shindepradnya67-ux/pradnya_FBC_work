## Write a program to reverse three-digit number

##Program

num=int(input('Enter a three-digit number : '))

d1=num//100
d2=(num//10)%10
d3=num % 10

reverse = d3*100+d2*10+d1
print('Reversed Number = ',reverse)