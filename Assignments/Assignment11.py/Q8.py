num=1
for i in range(1,11):
    if i%2!=0:
        for j in range(1,11):
            print(num,end=" ")
            num+=1
    else:
        start=num+9
        for j in range(1,11):
            print(start,end=" ")
            start-=1
        num+=10
    print()