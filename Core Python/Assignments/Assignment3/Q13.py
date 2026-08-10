## write a program to input electricity unit charges and calculate total electricity unit charges and
#  calculate total electricity bill according to the given condition:
#For first 50 units RS.0.50/unit
#For next 100 units Rs.1.20/unit
#For unit above 250 Rs.1.50/unit
#An additional surcharge of 20% is added to the bill

#Program : 

units = int(input("Enter Units : "))

## if units are up to 50 , the rate is o.50 per unit

if units <= 50:
    bill = units*0.50

## if units are up to 50, the rate is 0.50 per unit

elif units <=150:
    bill = (50*0.50)+(units-50)*0.75

## if units are between 51 and 150 , the first 50 units are charged at 0.50 , and the remaining units at 0.75

elif units <=250:
    bill = (50*0.50) + (100*0.75) + (units - 150)*1.20

## if units are between 151 and 250 ,the first 150 units are charged and the remaining units at 1.20

else : 
    bill = (50*0.50) + (100*0.75) + (100*1.20) + (units - 250) * 1.50

## if units are above 250 , the remaining units are charged at 1.50 per unit

bill = bill + (bill*20/100)

#Adds 20% surcharge to the bill.

print("Electricity Bill = ",bill)