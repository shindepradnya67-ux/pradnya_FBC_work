## python program to find the second largest number in the list using bubble sort
def bubblesort(li):
    size=len(li)
    for i in range(0,size):
        for j in range(0,size-1):
            if li[j]>li[j+1]:
                li[j],li[j+1]=li[j+1],li[j]
li=[10,50,30,80,20]
bubblesort(li)
print("Sorted list=",li)
print("Second largest=",li[-2])