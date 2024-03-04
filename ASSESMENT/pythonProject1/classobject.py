# class Person:
#     name = 'Jay'
#     age = 18
#     gender = 'Male'
#     marital_status = 'Complicated'
#     location = 'NY'
# print(Person.name)
# print(Person.age)
# print(Person.gender)
# print(Person.marital_status)
# print(Person.location)
# Person.age = 20
# print(Person.age)
#
# class Employees:
#     first_name = 'Florian'
#     last_name = 'Writz'
#     age = 23
#     Salary = 200000
#     gender  = 'Male'
# print(f'{Employees.first_name} {Employees.last_name} you are {Employees.age} and you earn {Employees.Salary} per month and you are {Employees.gender}.')
# print(f'{Employees.last_name} you are {Employees.gender}

# class Parents:
#     def __init__(self,firstname, lastname, age):
#         self.firstname = firstname
#         self.lastname = lastname
#         self.age = age
# Parent1 = Parents('John', 'Casii' , 45)
# Parent2 = Parents('Ann','Hathaway', 26)
# Parent3 = Parents('Luupita', 'Nyaks', 34)
# print(Parent1.firstname)
# print(Parent2.firstname)
# print(Parent3.firstname)
# print(Parent3.lastname)
# print(Parent1.lastname)
# print(Parent2.lastname)
# print(Parent2.age)
#
# class Cars:
#     def __init__(self,make,model,year):
#         self.make = make
#         self.model = model
#         self.year = year
# car1 = Cars('Ford','Mustang',1982)
# car2 = Cars('Chevrolet','Shelby',1966)
# car3 = Cars ('Dodge','Demon',2002)
# print(car1.make)
# print(car2.make)
# print(car3.make)
#
# print(f'My car model {car1.make}{car1.model} manufactred in {car1.year}')
# print(f'{car1.make}, {car2.make} and {car3.make} are all American car')
#
# class Students:
#     def __init__(self,Name, Age, Form):
#         self.Name = Name
#         self.Age = Age
#         self.Form = Form
# student1 = Students('Justus',19,4)
# student2 = Students('Robert',18,4)
# student3 = Students('Ethan',17,4)
# print(student1.Name)
# print(student2.Name)
# print(student3.Name)
#
# print(f'The following:{student1.Name}, {student2.Name} and {student3.Name} are all students of our institution. The above name are all form 4 students and are {student1.Age}, {student2.Age} and {student3.Age} years old respectively.')

# class Magari:
#     def __init__(self,make,model,price,year):
#         self.make =make
#         self.model = model
#         self.price = price
#         self.year  = year
#     def describe(self):
#         print(f'My favourite car is {self.make} {self.model}  priced at {self.price}')
# obj1 = Magari('Nissan','skyline',2100000,2013)
# obj2 = Magari('Toyota','Supra',2200000,2002)
# obj3 = Magari('Mazda','RX7',1800000,2014)
# print(obj1.describe())
# print(obj2.describe())
# print(obj3.describe())


class Person:
    def __init__(self,firstname,lastname,gender,age):
        self.firstname = firstname
        self.lastname = lastname
        self.gender = gender
        self.age = age
    def fullname(self):
        print(f'{self.firstname} {self.lastname}')
    def diaplay_age(self):
        print(self.age)
    def age_increase(self):
        self.age +=10
obj1 = Person('Francesco', ' Totti' ,'male',24)
obj1.age_increase()
print(obj1.fullname())
print(obj1.diaplay_age())
print(obj1.firstname)
print(obj1.gender)
print(obj1.lastname)
print(obj1.age_increase())