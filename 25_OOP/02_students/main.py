from Groupe import StudentList, Student

student_1 = Student('Sam', '1', '1 2 3 4 5')
student_2 = Student('Petya', '2', '3 4 5 3 4')
student_3 = Student('Vasya', '3', '5 2 3 4 5')
student_4 = Student('Dan', '2', '4 3 4 4 5')
student_5 = Student('Lisa', '4', '2 2 2 4 5')
student_6 = Student('Natasha', '2', '1 2 2 3 2')
student_7 = Student('Igor', '1', '2 4 3 4 3')
student_8 = Student('Gena', '2', '2 2 3 4 3')
student_9 = Student('Dina', '3', '3 4 3 4 4')
student_10 = Student('Andrew', '2', '5 3 3 4 5')

s_group = (student_1, student_2, student_3, student_4, student_5, student_6, student_7, student_8, student_9, student_10)

for i_student in s_group:
    i_student.info()

# если хотим использовать заполнение через консоль:
# s_group = StudentList(2)
# s_group.fill()