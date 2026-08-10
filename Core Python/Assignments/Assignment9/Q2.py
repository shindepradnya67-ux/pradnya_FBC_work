## 2.WAP to check given number is Armstrong or not using recursive function
def armstrong (temp,digits):
    if temp==0:
        return 0
    rem=temp%10
    return(rem**digits)+armstrong(temp//10,digits)
num=int(input("Enter a number : "))
digits = len(str(num))

res=armstrong(num,digits)
if res==num:
    print("Armstrong Number")
else:
    print("Not Armstrong Number")