## WAP to create a duplicate of an existing list . it should not point to same list.
li=[10,20,30,40]
new_li=[]
for i in range(0,len(li)):
    new_li+=[li[i]]
print("Original list:",li)
print("Duplicate list: ",new_li)