## WAP to create three lists of numbers,their squares and cubes
li=[2,3,4,5]
square=[]
cube=[]
for i in range(0,len(li)):
    square+=[li[i]**2]
    cube+=[li[i]**3]
print("Number List=",li)
print("Square List=",square)
print("Cube List=",cube)