## Python program to put even and odd element of a list into two different lists.
li=[2,5,6,10,12,13,14,16,18,20,30]
even=[]
odd=[]
for i in range(0,len(li)):
    if li[i]%2==0:
        even+=[li[i]]
    else:
        odd+=[li[i]]
print("Even list=",even)
print("Odd list=",odd)
