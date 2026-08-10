## Enter number of students from user for those many students accepts marks of 5 subject marks from user and calculate percentage.
## Display all percentage and average percentage of students

## Program : 
n = int(input("Enter number of students : "))
total_per = 0

for i in range(1,n+1):
    print()
    print("student",i)

    m1 = int(input("Enter marks of subject1 : "))
    m2 = int(input("Enter marks of subject2 : "))
    m3 = int(input("Enter marks of subject3 : "))
    m4 = int(input("Enter marks of subject4 : "))
    m5 = int(input("Enter marks of subject5 : "))

    total = m1+m2+m3+m4+m5 
    percentage = total/5

    print("percentage=",percentage)

    total_per = total_per + percentage
average = total_per / n
print()
print("Average percentage = ",average )


