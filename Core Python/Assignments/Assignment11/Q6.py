##Python program to find the union of two lists.
li1=[10,20,30,40]
li2=[30,40,50,60]
union=[]
for i in range(0,len(li1)):
    if li1[i] not in union:
        union+=[li1[i]]
for i in range(0,len(li2)):
    if li2[i] not in union:
        union+=[li2[i]]
print("Union=",union)
