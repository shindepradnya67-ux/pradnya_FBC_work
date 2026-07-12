##WAP to calculate area of triangle and rectangle .
## Program

## Input for triangle
base = float(input('Enter base of a trianlge : '))
height = float(input('Enter height of triangle : '))

## Calculate area of trianlge
triangle_area = (base*height)/2

##Input for rectangle
length = float(input('Enter length of rectangle : '))
breadth = float(input('Enter breadth of rectangle : '))

##Calculate area of rectangle 
rectangle_area = length*breadth

##Display the result
print('Area of Triangle = ',triangle_area)
print('Area of Rectangle = ',rectangle_area)