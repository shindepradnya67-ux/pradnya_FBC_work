##Write a program to enter P,T,R and calculate simple interest
#Formula
#SI=(P×T×R)/100
#Where:
#P = Principal Amount
#T = Time (in years)
#R = Rate of Interest (%)
#SI = Simple Interest
# Algorithm
# Start.
# Input Principal (P), Time (T), and Rate (R).
# Calculate Simple Interest:
# SI = (P * T * R) / 100
# Display the Simple Interest.
# Stop.

## Program :
P = int(input('Enter Principle Amount : '))
R = int(input('Enter Rate of Interest : '))
T = int(input('Enter Time (in years ): '))

SI = (P*T*R)/100

print("Simple Interest ",SI)