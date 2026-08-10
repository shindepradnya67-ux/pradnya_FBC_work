## Python program to sort the list according to the second element in sublist.
li=[[1,50],[2,20],[3,40],[4,10]]
for i in range (1,len(li)):
    for j in range(0,len(li)-i):
        if li[j][1]>li[j+1][1]:
            li[j],li[j+1]=li[j+1],li[j]
print("Sorted List=",li)