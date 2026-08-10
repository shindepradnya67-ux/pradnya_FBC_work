## WAP of having n number of element in the list and find out even and odd element in that list and then create two 
# separate lists which will have even element and other which will have even elements and other list have odd elements.

n=int(input("Enter the number element: "))
li=[]
for i in range(1,n+1):
    num=int(input(f"Enter the number{i}: "))
    li+=[num]
even=[]
odd=[]
for i in range(0,len(li)):
    if li[i]%2==0:
        even+=[li[i]]
    else:
        odd+=[li[i]]
print("Original list=",li)
print("Even list=",even)
print("odd list=",odd)
