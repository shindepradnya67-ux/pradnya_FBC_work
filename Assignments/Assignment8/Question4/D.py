# with parameter + with return

def odd_sum(n):
    sum=0
    for i in range(1,n+1,2):
        sum=sum+i
    return sum
num=int(input("Enter the number : "))
ans=odd_sum(num)
print(ans)