#without parameter + with return
def rectangle():
    length=int(input("Enter the length : "))
    breadth = int(input("Enter the breadth : "))

    Area=length*breadth
    return Area
ans=rectangle()
print("Area of rectangle is : ",ans)