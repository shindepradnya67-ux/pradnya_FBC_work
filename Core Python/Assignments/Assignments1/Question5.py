## Write a Program to enter P,T,R and calculate Compound Interest

# Program 

P = float(input('Enter principal Amount : '))
R = float(input('Enter Rate of Interest : '))
T = float(input('Enter Time(in years) : '))

A = P*(1+R/100)**T
CI = A-P
print ("Compound Interest = ",CI)