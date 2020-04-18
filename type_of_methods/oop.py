class Employee:
    hike = 1.04  # class variables

    def __init__(self, name, sal):
        # instance variables
        self.name = name
        self.sal = sal

    def emp_details(self):
        return f'emp name: {self.name}, sal: {self.sal}, hike: {self.hike}'

    @classmethod
    def init_emp(cls, emp_str):
        name, sal = emp_str.split(',')
        return cls(name, sal)

    @staticmethod
    def feeling(feel):
        print(f'You are feeling {feel}!!')


# regular method
e1 = Employee('Abhi', 75)
print(f'emp e1 details : {e1.emp_details()}')

# class method
emp_str = "shek, 80"
e2 = Employee.init_emp(emp_str)
print(f'emp e1 details : {e2.emp_details()}')

# static method
Employee.feeling('happy')
