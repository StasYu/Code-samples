class Student:

    def __init__(self, name='SomeName', group='Some group', grades='0', index=0):
        self.index = index
        self.name = name
        self.group = group
        self.grades = grades.split()

    def info(self):
        if len(self.grades) > 0:
            for i in self.grades:
                self.grades[self.grades.index(i)] = int(i)
        self.avrg = sum(self.grades) / len(self.grades)

        print(f'\nname: {self.name}, group: {self.group}, grades: {self.avrg}')

class StudentList:
    def __init__(self, count):
        self.students = [Student(index=i_index) for i_index in range(1, count + 1)]

    def all_info(self):
        for i_student in self.students:
            i_student.info()

    def fill(self):
        for i_student in self.students:
            i_student.name = input('\nName Surname: ')
            i_student.group = input('Group: ')
            i_student.grades = input('5 Grades separated by space: ').split(' ')
        self.all_info()