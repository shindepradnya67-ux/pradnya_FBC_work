## e] x-x 2/3 + x 3/5 - x 4/7 + ..... to n terms 

##Program : 
x = int(input("Enter x : "))
n = int(input("Enter number of terms : "))

sum = 0
sign = 1
den = 1

for i in range(1,n+1):
    sum = sum + sign * (x ** i)/den
    sign = sign * -1
    den = den + 2
print("sum = ",sum)
