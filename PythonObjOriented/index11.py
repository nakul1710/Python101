     # Nested class: Class defined within another class 
     #   class Outer:
     #       class Inner:
     #
     # Benefits - Allows you to logically group classes that are closely related 
     #            Encapsulate private detail that aren't relevant outside the class
     #            Keeps the namespace clean


class Company:
    class Employee:
        def __init__(self, name, position):
            self.name = name
            self.position = position

        def get_details(self):
            return f"{self.name} {self.position}"

    def __init__(self, company_name):
        self.company_name = company_name
        self.employees = []  # Fixed typo: employee -> employees

    def add_employee(self, name, position):
        new_employee = self.Employee(name, position)
        self.employees.append(new_employee)

    def list_employees(self):
        return [employee.get_details() for employee in self.employees]

company = Company("Macdonald")

company.add_employee("Eugene", "Manager")
company.add_employee("spangbob", "Cook")
company.add_employee("Squidward", "Casier")

for employee in company.list_employees():
    print(employee)
