#WAP to print all number which are divisible by m and n in the list.

li=[10,20,23,15,18,20,24,30]
m=int(input("Enter the number : "))
n=int(input("Enter the number : "))
for i in range(0,len(li)):
    if li[i]%m==0 and li[i]%n==0:
        print(li[i])
