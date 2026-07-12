## Write a program to input two angles from user and find third angle of the triangle 

# Program :

A1 = float(input('Enter first angle : '))
A2 = float(input('Enter second value : '))
A3 = 180 - (A1+A2)

print('Third angle of triangle is = ',A3)