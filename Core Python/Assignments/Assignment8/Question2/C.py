## without parameter + with return
def circle():
    r=int(input("Enter the radius : "))
    Area = 3.14*r*r
    return Area

ans=circle()
print("Area of circle: ",ans)