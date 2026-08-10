#with parameter + with return
def circle(r):
    Area  = 3.14*r*r
    return Area
radius = int(input("Enter the radius : "))
ans=circle(radius)
print("Area of circle is : ",ans)