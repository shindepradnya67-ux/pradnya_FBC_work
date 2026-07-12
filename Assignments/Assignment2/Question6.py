##WAP to calculate total salary of employee based on basic . DA=10% of basic,HRA=15% of basic,TA=12% of basic.
#Program
basic=float(input('Enter Basic salary : '))
da =basic*0.10
hra =basic*0.15
ta =basic*0.12

total=basic+da+hra+ta
print('Total salary = ',total)
