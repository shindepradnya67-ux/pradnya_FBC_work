## WAP to create three list of numbers,their squares and cubes
li=[2,3,4,5,6,7,8]
square=[]
cube=[]
for i in range(0,len(li)):
    cube+=[li[i]**3]
    square+=[li[i]**2]
print("Number list=",li)
print("Square list=",square)
print("Cube list=",cube)