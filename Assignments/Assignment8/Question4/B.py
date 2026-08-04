# with parameter + without return
def odd_sum(n):
    sum=0
    for i in range(1,n+1,2):
        sum=sum+i
    print("Sum=",sum)
num=int(input("Enter the num : "))
odd_sum(num)