# age = int(input('How old are you?' ))
# if age >= 65:
#     print('Your days are numbered')
# elif age < 65 and age >= 50:
#     print('Almost there')
# elif age < 40 and  age >=18:
#     print('You are safe')
# else:
#     print('Go back home')

# marks = float(input('Enter your marks '))
# if marks >=80 and marks<=100:
#     print('You have an A')
# elif marks >=60 and marks <=79:
#     print('You have a B')
# elif marks >=50 and marks <=69:
#     print('You have a C')
# elif marks >=40 and marks <=49:
#     print('You have an D')
# elif marks >=0 and marks <=39:
#     print('You have an E')
# else:
#     print('Enter valid marks (0-100)')
temperature = float(input('What is your body temperature? '))
if temperature >= 30:
    print('Put on a vest')
elif temperature >=20 and temperature <=29:
    print('Have a sweater on')
elif temperature <20:
    print('Put on your jacket')
else:
    print('Enter a valid body temperature')