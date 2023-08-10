class Person:
    def __init__(self, name, surname, age):
        self.__name = name
        self.__surname = surname
        self.__age = age

    def get_name(self):
        return self.__name

    def get_surname(self):
        return self.__surname

    def get_age(self):
        return self.__age

class Employee(Person):

    def info(self):
        print(f'\nname: {self.get_name()}\n'
              f'Surname: {self.get_surname()}\n'
              f'Age: {self.get_age()}')

    def salary_calculation(self):
        pass

class Manager(Employee):
    def __init__(self, name, surname, age):
        super().__init__(name, surname, age)
        self.__salary = 13 * 10 ** 3

    def info(self):
        super().info()
        print(f'Salary: {self.__salary}')
class Agent(Employee):
    def __init__(self, name, surname, age):
        super().__init__(name, surname, age)
        self.__sales = self.sales_amount()
        self.__salary = self.salary_calculation()

    def info(self):
        super().info()
        print(f'Salary: {self.__salary}')

    def sales_amount(self):
        sales = int(input('\nAgent:\ninput sales amount: '))
        return  sales
    def salary_calculation(self):
        percentage = self.__sales * 5 / 100
        salary = 5*10**3 + percentage
        return salary

class Worker(Employee):
    def __init__(self, name, surname, age):
        super().__init__(name, surname, age)
        self.__hours = self.hours_count()
        self.__salary = self.salary_calculation()

    def info(self):
        super().info()
        print(f'Salary: {self.__salary}')

    def hours_count(self):
        hours = int(input('\nWorker:\nInput hours worked: '))
        return hours

    def salary_calculation(self):
        salary = 100 * self.__hours
        return salary

emp_1 = Worker(name='Tom', surname='Robbins', age=22)
emp_2 = Worker(name='Bob', surname='Bobbins', age=34)
emp_3 = Worker(name='Sara', surname='Mills', age=25)
emp_4 = Agent(name='Lucy', surname='Hi', age=27)
emp_5 = Agent(name='John', surname='Travolta', age=46)
emp_6 = Agent(name='Sam', surname='Smith', age=30)
emp_7 = Manager(name='Jackie', surname='Chan', age=52)
emp_8 = Manager(name='Gal', surname='Gadot', age=31)
emp_9 = Manager(name='Margot', surname='Robbie', age=28)

emp_1.info()
emp_2.info()
emp_3.info()
emp_4.info()
emp_5.info()
emp_6.info()
emp_7.info()
emp_8.info()
emp_9.info()