Height = float(input('What is your height in metres? '))
Mass = float(input('What is your mass im kilograms? '))
print(Height,Mass)
BMI = Mass/(Height*Height)
print(BMI)
if BMI <=18:
    print('You are underweight')
elif BMI >=19 and BMI <=25:
    print('You are Normal')
elif BMI >=26 and BMI <=30:
    print('You are Overweight')
elif BMI >30:
    print('You are obese')
else:
    print('Enter valid values')
print( BMI)