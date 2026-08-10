#1. Write a program to find the area and perimeter of following figure (Accept the
#length, breadth and radius from user:

l = float(input("Enter length: "))
b = float(input("Enter breadth: "))
r = float(input("Enter radius: "))

area_rectangle = l * b
area_semicircle = 3.14 * r * r / 2

area = area_rectangle + area_semicircle

perimeter = (2 * l) + b + (3.14 * r)

print("Area =", area)
print("Perimeter =", perimeter)