# print('this is my first function')
# print('this is my first function')
# print('this is my first function')

# def once():
#     print('this my first function')
#     print('this is my first function')
#     print('this is my first function')
# once()

# def my_name(name):
#     print(name)
#     print(name)
#     print(name)
# my_name('Kim')
# my_name('Jesse')
# my_name('Jose')
#
# def num(nambari):
#     print(nambari)
#     print(nambari)
# num(45)
# num(56)
#
# def salutations(first_name):
#     print( ' Hi' + first_name  +  ' Holla papi')
# salutations(' Joje')
#
# def miaka(age):
#     print('Hello, you ' + str(age) + ' years old')
# miaka(22)
#
# def my_name(first_name , last_name):
#     print(first_name +  last_name + ' is the greatest rapper alive .')
# my_name("Kendrick",' Lamar')
#
# def sentence(first_name , last_name, age):
#     print(first_name + '' + last_name + ' is ' +  str(age) + ' years old')
# sentence(' luke',' combs',  16)
#
# def employees(name,age):
#     if age>=20:
#         print(name + ' you are ' + str(age)+ ' years old')
#     elif age<20 and age>=15:
#         print(name + 'you are' + str(age) + 'years old')
#     elif age<15 and age>=10:
#         print(name + 'you are' + str(age) + ' years old')
#     else:
#         print('You are not yet born')
# employees('Kendall',12)
# employees('elly',34)
#
# def age_calculation(age):
#     new_age = age +10
#     return new_age
# print(age_calculation(23))
#
# def marks_calculator(*subjects):
#     total_marks = sum(subjects)
#     return total_marks
# print(marks_calculator(23,45,67))
# print(marks_calculator(2,56,68,89))
# print(marks_calculator(90,88))

def marks(name,comp,math):
    total = int(comp+math)
    return total
print(marks('Mark',80,88))

def workers(age):
    if age >60:
        print(' Relocate to Kisumu')
    elif age>=50 and age <=59:
        print(' Move to Nakuru')
    elif age >=30 and age <=49:
        print(' Move to Mombasa')
    else:
        print(' Move to Nairobi')
workers(24)

def country(nchi='Kenya'):
    return nchi
print(country('Tanzania'))+
print(country('Uganda'))
print(country('Russia'))
print(country())



























