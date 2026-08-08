## WAP to print list after removing even numbers 

li=[10,15,20,25,30,35]
new_li=[]
for i in range(0,len(li)):
    if li[i]%2 !=0:

        new_li+=[li[i]]
print("List after removing even number=",new_li)