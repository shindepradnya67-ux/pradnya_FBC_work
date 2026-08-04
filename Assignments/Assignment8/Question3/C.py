## C. 1^1+2^2+3^3+4^4....n^n
## without parameter + without return
# def power_sum():
#     n=int(input("Ente the n : "))
#     sum=0

#     for i in range(1,n+1):
#         sum=sum+(i**i)
#     print("Sum=",sum)
# power_sum()    

## with parameter + without return

# def power_sum(n):
#     sum=0
#     for i in range(1,n+1):
#         sum=sum+(i**i)
#     print("Sum=",sum)
# num=int(input("Enter the num : "))
# power_sum(num)

## without parameter + with return

# def power_sum():
#     n=int(input("Enter the number : "))
#     sum=0
#     for i in range(1,n+1):
#         sum=sum+(i**i)
#     return sum
# ans=power_sum()
# print("sum=",ans)

## with parameter + with return

def power_sum(n):
    sum=0
    for i in range(1,n+1):
        sum=sum+(i**i)
    return sum
num=int(input("Enter the num : "))
ans=power_sum(num)
print("Sum=",ans)
 
