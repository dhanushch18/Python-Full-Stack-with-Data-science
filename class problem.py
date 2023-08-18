
class person:
    def __init__(employee,name,age,salary):
        employee.name=name
        employee.age=age
        employee.salary=salary
    def func(company):
        print("The name of the employee is "+company.name)

    def __str__(employee):
        return f"age is {employee.age} and salary is {employee.salary}"
#print("His age is "+company.age)
#rint("Salary :"+company.salary)
p1=person("Raju",40,35000)
p1.func()
print(p1)