## WAP to print list after removing even numbers
li=[10,20,3,45,6,7,8,9,22,12,33]
new_li=[]
for i in range(0,len(li)):
    if li[i]%2!=0:
        new_li+=[li[i]]
print("List after removing even numbers: ",new_li)