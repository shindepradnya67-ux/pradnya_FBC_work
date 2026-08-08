# WAP to find the maximum and minimum element in list
li=[10,40,50,80,90,91]
max=li[0]
min=li[0]
for i in range(0,len(li)):
    if li[i]>max:
        max=li[i]
    if li[i]<min:
        min=li[i]
print("Maximum element of list: ",max)
print("Minimum element of list:",min)