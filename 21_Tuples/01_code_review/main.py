students = {
    1: {
        'name': 'Bob',
        'surname': 'Vazovski',
        'age': 23,
        'interests': ['biology, swimming']
    },
    2: {
        'name': 'Rob',
        'surname': 'Stepanov',
        'age': 24,
        'interests': ['math', 'computer games', 'running']
    },
    3: {
        'name': 'Alexander',
        'surname': 'Krug',
        'age': 22,
        'interests': ['languages', 'health food']
    }
}


# def f(dict):
#     lst = []
#     string = ''
#     for i in dict:
#         lst += (dict[i]['interests'])
#
# # pairs = []
# # for i in students:
# #     pairs += (i, students[i]['age'])
# #
# #
# # my_lst = f(students)[0]
# # l = f(students)[1]
# # print(my_lst, l)

string = []
surname_len = int()
for i_count, i_items in students.items():
    string.extend(i_items['interests'])
    surname_len += len(i_items['surname'])

print(string, surname_len)


