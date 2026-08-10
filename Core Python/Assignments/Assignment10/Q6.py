## WAP to remove duplicates from the list.
li=[10,20,30,40,50,60,20,30,40]
new_li=[]
for i in range(0,len(li)):
    if li[i] not in new_li:
        new_li+=[li[i]]
print("remove duplicate list:",new_li)