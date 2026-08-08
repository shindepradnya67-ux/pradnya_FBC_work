## WAP to create a new list from existing list. which contain cube of each number of list .
li=[2,3,4,5,6,7,8,9]
cube=[]
for i in range(0,len(li)):
    cube+=[li[i]**3]
print("Cube of list",cube)

