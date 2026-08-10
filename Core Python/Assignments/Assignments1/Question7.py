## Program to find the Roots of a Quadratic Equation
import math

a=float(input('Enter value of a : '))
b=float(input('Enter value of b : '))
c=float(input('Enter value of c : '))

##Calculate the discriminant
d=b*b-4*a*c
root1=(-b+math.sqrt(d))/(2*a)
root2=(-b-math.sqrt(d))/(2*a)

print("first Root=",root1)
print("second Root=",root2)