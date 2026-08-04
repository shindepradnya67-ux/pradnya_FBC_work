#sum of all odd numbers between 1 to n
# EX: n=10
# odd number = 1 3 5 7 9
# sum = 1+3+5+7+9=25

# without parameter + without return
def odd_sum():
    n=int(input("Enter the number : "))
    sum=0
    for i in range(1,n+1,2):
        sum=sum+i
    print("Sum=",sum)
odd_sum()

# with parameter + without return
def odd_sum(n):
    sum=0
    for i in range(1,n+1,2):
        sum=sum+i
    print("Sum=",sum)
num=int(input("Enter the num : "))
odd_sum(num)


# without parameter + with return
def odd_sum():
    n=int(input("Enter the n : "))
    sum=0
    for i in range(1,n+1,2):
        sum=sum+i
    return sum
ans=odd_sum()
print(ans)

# with parameter + with return

def odd_sum(n):
    sum=0
    for i in range(1,n+1,2):
        sum=sum+i
    return sum
num=int(input("Enter the number : "))
ans=odd_sum(num)
print(ans)
