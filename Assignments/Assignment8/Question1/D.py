## with parameter + with Return

def rectangle(length,breadth):
    Area=length*breadth
    return Area
l=int(input("Enter the length of rectangle : "))
b=int(input("Enter the breadth of rectangle : "))
ans=rectangle(l,b)
print("Area of rectangle is ",ans)