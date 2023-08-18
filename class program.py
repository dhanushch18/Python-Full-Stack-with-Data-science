class person:
    def __init__(employee,name,age,salary):
        employee.name=name
        employee.age=age
        employee.salary=salary

    def __str__(self):
        return f"{self.name}({self.age})"
p1=person("Dhanush",22)
print(p1)