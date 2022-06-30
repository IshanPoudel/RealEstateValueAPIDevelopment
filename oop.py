class Employee:
    raise_amount = 1.4
    def __init__(self , first , last , pay):  #similar to this
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    @classmethod
    def from_string(cls , emp_str):
        first , last , pay = emp_str.split('-')
        return cls(first , last , pay)


    def printclass(self):
        print(self.first)
        print(self.last)
        print(self.pay)
        print(self.email)

    def fullname(self):
        return '{} {}'.format(self.first , self.last)
    def apply_raise(self):
        self.pay = int (self.pay*self.raise_amount)

    @classmethod
    def set_raise_amt (cls , amount):
        cls.raise_amount = amount
    @staticmethod
    def is_workdat(day):
        if day.weekday()==5 :
            return true
        return false



emp_1 = Employee('Cprey' , 'Schafwer' , 50000)

emp_2 = Employee('Test' , 'User' , 60000)



Employee.set_raise_amt(1.08)


print(emp_1.raise_amount)
print(Employee.raise_amount)
print(emp_2.raise_amount)

emp_1.raise_amount = 1.05


emp_str_1 = 'john-doe-70000'
new_employee = Employee.from_string(emp_str_1)

new_employee.printclass()

class Developer(Employee):
    raise_amount =  1.80

    def __init__(self , first , last , pay , prog_lang):
        super().__init__(first , last , pay)
        self.prog_lang = prog_lang


class Manager(Employee):
    raise_amount = 1.9

    def __init__(self , first , last , pay , emmployees=None):





dev_1 = Developer('Corey' , 'Schafer' , 50000)
dev_2 = Developer('Test' , 'Employee' , 60000)

print(dev_1.pay)
dev_1.apply_raise()
print(dev_1.pay)
