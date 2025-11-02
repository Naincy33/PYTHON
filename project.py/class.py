class Programmer:
    company="Microsoft"
    def __init__(self, name, salary, pin):
       self.name= name
       self.salary= salary
       self.pin= pin

p= Programmer("NANO",1300000,560004)
print(p.name, p.salary, p.pin, p.company)
