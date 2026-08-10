## WAP to check given number is Armstrong or not.

no = int(input("Enter No : "))
count = len(str(no))
print(count)
temp=no
rev = 0
while no>0:
    d = no %10
    rev = rev +(d**count)
    no = no//10
if rev == temp:
    print("The number is Armstrong")
else :
    print("The number is not Armstrong")