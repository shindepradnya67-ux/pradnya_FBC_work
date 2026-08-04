#b] 1!+2!+3!+4!......+n!
# without parameter + without return
# def factorial_num():
#     num=int(input("Enter the number : "))
#     sum=0
#     for i in range(1,num+1):
#         fact=1
#         for j in range(1,i+1):
#             fact=fact*j
#         sum=sum+fact
#     print("Sum=",sum)
# factorial_num()

#with parameter + without return
# def factorial(num):
#     sum=0
#     for i in range(num+1):
#         fact=1
#         for j in range(1,i+1):
#             fact=fact*j
#         sum=sum+fact
#     print("sum=",sum)
# n=int(input("Enter n : "))
# factorial(n)

#without parameter + with return
# def factorial_num():
#     num=int(input("Enter the number : "))
#     sum=0
#     for i in range(1,num+1):
#         fact=1
#         for j in range(1,i+1):
#             fact=fact*j
#         sum=sum+fact
#     return sum
    
# ans=factorial_num()
# print("Sum=",ans)

#with parameter + with return
def factorial_num(n):
    sum=0
    for i in range(1,n+1):
        fact=1
        for j in range(1,i+1):
            fact=fact*j
        sum=sum+fact
    return sum
num=int(input("Enter the num : "))
ans=factorial_num(num)
print("Sum=",ans)
