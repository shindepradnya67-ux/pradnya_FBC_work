## Write a program to check if person is eligible to marry or not (male age >=21 and female age>=18)
gender = input('Enter gender(m/f): ')
age = int(input('Enter age : '))

if(gender == 'f'):
    if(age>=18):
        print("Girl is eligible for marriage")
    else:
        print("Pehle padhai kar lo")
else:
    if(age>=21):
        print('Boy is eligible for marriage')
    else:
        print('Pehle kama lo')