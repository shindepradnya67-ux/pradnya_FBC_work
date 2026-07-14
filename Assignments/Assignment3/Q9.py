## Input 5 Subject Marks and Display Grade
m1=int(input('Enter marks of subject 1 : '))
m2=int(input('Enter marks of subject 2 : '))
m3=int(input('Enter marks of subject 3 : '))
m4=int(input('Enter marks of subject 4 : '))
m5=int(input('Enter marks of subject 5 : '))

ObtainedMarks = m1+m2+m3+m4+m5
Total = 500
per= ObtainedMarks/Total*100

print("Total Marks = ",ObtainedMarks)
print("Percentage = ",per)

if per>=75:
    print("Grade : Distinction")
elif per>=60:
    print("Grade : First Class")
elif per>=50:
    print("Grade:Second class")
elif per>=35:
    print("Grade:pass class")
else:
    print("Grade:fail")
