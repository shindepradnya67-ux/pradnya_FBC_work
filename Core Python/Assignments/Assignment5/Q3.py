## Accept no.of passengers from user and per ticket cost. Then accept age of each passenger and then calculate total amount to 
## ticket to travel for all of them based on following condition : 
# a.children below 12=30% discount
# b.senior citizen (abov 59)=50% discount
# c.others need to pay full.

n = int(input("Enter number of passengers : "))
cost = int(input("Enter ticket cost : "))

total = 0
for i in range(1,n+1):
    print()
    age = int(input("Enter age of passengers{}:".format (i)))

    if age<12:
        fare = cost-(cost*0.30)

    elif age>59:
        fare = cost-(cost*0.50)
    else:
        fare = cost
    print("Ticket fare= ",fare)
    total = total+fare
print()
print("Total ticket Amount=",total)