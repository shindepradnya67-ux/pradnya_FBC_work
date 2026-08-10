## Accept a number from user and check if this element is present in the list or not also tell how many times ti is present in the list.
li=[10,20,30,40,50,60,20,30,40]
count=0
num=int(input("Enter number : "))

for i in range(0,len(li)):
    if li[i]==num:
        count=count+1
if count>0:
    print("Element is present in list")
    print("Count=",count)
else:
    print("Element is not present")
    