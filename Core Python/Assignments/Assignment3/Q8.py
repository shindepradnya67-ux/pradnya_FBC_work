## Write a program to prompt user to enter userid and password.After verifying userid and password display a 4 digit random number
#  and ask user to enter the same.
# If user enters the same number then show him success message otherwise failed. (Something like captcha)
import random
userid = input('Enter userid : ')
password = input('Enter password : ')

if userid =='admin' and password == 'Rsml@1234':
    captch=random.randint(1000,9999)
    print(f"Your Captcha={captch}")
    chuser=int(input("Enter the Captcha=>"))
    if chuser==captch:
        print("User Login Successfully...")
    else:
        print("Invalid Captcha....")
else:
    print("User is Invalid")
    