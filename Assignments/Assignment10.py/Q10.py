## WAP to remove all occurence of a given element in the list
li=[10,20,30,40,20,30,40,50,60]
num=int(input("Enter the number: "))
new_li=[]
for i in range(0,len(li)):
    if li[i]!=num:
        new_li+=[li[i]]
print("List after removing=",new_li)
