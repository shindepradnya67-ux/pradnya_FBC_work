# without parameter + with return
def odd_sum():
    n=int(input("Enter the n : "))
    sum=0
    for i in range(1,n+1,2):
        sum=sum+i
    return sum
ans=odd_sum()
print(ans)
