## Check whether a Triangle is valid (Using Sides)
a= int(input('Enter first side : '))
b= int(input('Enter second side : '))
c= int(input('Enter third side : '))

if a+b>c and a+c>b and b+c>a : 
    print('valid Triangle')
else : 
    print('Invalid Triangle')