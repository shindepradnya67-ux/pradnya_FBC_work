## Write a program to check correct user ID and Password . 

userid = input('Enter userid : ')
password = input('Enter password : ')

if userid == "admin" and password == "Rsml@123" :
    print('Login successful')
else :
    print('Invalid userid or password')