class Employees:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
class Receptionist(Employees):
    def __init__(self,name,salary,gender):
        super().__init__(name,salary)
        self.gender = gender
class Frontend_developer(Receptionist):
    def __init__(self,name,salary,gender,language):
        super().__init__(name,salary,gender)
        self.language = language
Receptionist1 = Receptionist('Hermoine',230000,'Female')
Employees1 = Employees('Albus',500000)
Developer1 = Frontend_developer('Maina',350000,'male','python')
print(Receptionist1.name)
print(Employees1.name)
print(Developer1.language)
