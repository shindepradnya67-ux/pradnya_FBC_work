## WAP to solve the following series:
## a] 1! + 2! + 3! + 4! + ......n!
## b] N + N^2 + N^3 + N^4 .... N^N(here ^ means exponent)
## c] Find the sum of geometric series from 1 to n where common ratio is 2.
## d] S = a + a 2/2 + a 3/3 + ... + a 10/10
## e] x-x 2/3 + x 3/5 - x 4/7 + ..... to n terms 

## a] 1! + 2! + 3! + 4! + ......n!

n = int(input("Enter n  : "))
sum = 0
fact = 1
for i in range(1,n+1):
    fact = fact * i
    sum = sum + fact 
    print ("sum = ",sum )
