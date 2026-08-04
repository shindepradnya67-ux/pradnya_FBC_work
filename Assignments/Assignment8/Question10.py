## WAP to check enterd year is leap year or not
# with parameter with return
def leap_year(year):
    if((year%400==0)or(year%4==0)and year%100!=0):
        return "Leap year"
    else:
        return "Not leap year"
num=int(input("Enter the num : "))
ans=leap_year(num)
print(ans)