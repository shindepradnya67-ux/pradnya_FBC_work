## Write a program to calculate the percentage of student based on marks of any 5 subject .

## Algorithm :
# 1. Start
# 2. Input marks of 5 subject (m1,m2,m3,m4,m5)
# 3. Calculate the obtained marks # obtained = m1+m2+m3+m4+m5
# 4. Set the total marks : Total = 500
# 5. Calculate the Percentage : ## Percentage = (obtained/Total)*100
# 6. Display the obtained marks and percentage
# 7. Stop

## Program :-

m1 = float (input('Enter marks of subject 1 : '))
m2 = float (input('Enter marks of subject 2 : '))
m3 = float (input('Enter marks of subject 3 : '))
m4 = float (input('Enter marks of subject 4 : '))
m5 = float (input('Enter marks of subject 5 : '))

Obtained = m1+m2+m3+m4+m5
Total = 500
Percentage = (Obtained/Total)*100
print("Obtained Marks ",Obtained)
print("Percentage = ",Percentage , "%")
