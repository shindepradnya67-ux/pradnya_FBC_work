def bubbleSort(li):
    size=len(li)
    for i in range(1,size):
        for j in range(0,size-i):
            if li[j]>li[j+1]:
                li[j],li[j+1]=li[j+1],li[j]
li1=[10,30,20]
li2=[40,5,25]
li=li1+li2
print("Before Sorting:",li)
bubbleSort(li)
print("After Sorting: ",li)


## or
li1 = [10, 30, 20]
li2 = [40, 5, 25]

li = li1 + li2

for i in range(0, len(li)):
    for j in range(0, len(li)-1-i):
        if li[j] > li[j+1]:
            li[j], li[j+1] = li[j+1], li[j]

print("Merged and Sorted List =", li)