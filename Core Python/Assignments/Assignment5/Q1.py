## WAP to prompt user to enter user id and password .If id and password is incorrect give him chance to
#  re-enter the credentials.Let him try 3 times . After that program to terminates . 

##program : 
uid = "admin"
pwd = "1234"

count = 1
while count<=3:
    user = input("Enter user ID : ")
    password = input("Enter Password : ")

    if user == uid and password == pwd:
        print("Login successful")
        break
    else :
        print("Invalid credentials")
        count=count+1
if count>3:
    print("Account Terminated") 