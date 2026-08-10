## Python program to sort a list according to the length of the elements within the list
li=["apple","cat","banana","hi"]
for i in range(1,len(li)):
    for j in range(0,len(li)-i):
        if len(li[j])>len(li[j+1]):
            li[j],li[j+1]=li[j+1],li[j]
print("Sorted list according to length=",li)