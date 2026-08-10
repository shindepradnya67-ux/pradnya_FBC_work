## WAP to check if a given number is armstrong number or not.for each task create separate functions.
def checkArmstrong(num):
    count=len(str(num))
    sum=0
    while num>0:
        d=num%10
        sum=sum+d**count
        num=num//10
    return sum
n=int(input("Enter the number: "))
checkArmstrong(n)
result=checkArmstrong(n)
if result==n:
    print(f"{n} is Armstrong")
else:
    print(f"{n} is no Armstrong")
