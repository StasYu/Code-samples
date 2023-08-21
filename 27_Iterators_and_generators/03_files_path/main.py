import os

root_path = os.path.abspath(os.path.join('..', '..'))
# print(root_path)
directory = os.path.abspath(os.path.join('main.py'))
# print(directory)
all_files = os.listdir(root_path)
# print(all_files)

def gen_files_path(root_path: str, listed: list[str]):
    for i_elem in listed:
        temp = os.path.join(root_path, i_elem)
        if os.path.isfile(temp):
            yield temp
        if os.path.isdir(temp):
            recursed = gen_files_path(root_path=temp, listed=os.listdir(temp))
            for i_num in recursed:
                yield i_num


file = open('directory_list.txt', 'w')
file.close()

new = gen_files_path(root_path=root_path, listed=sorted(all_files))
for i in new:
    if i == directory:
        print(i)
        break
    else:
        with open('directory_list.txt', 'a') as file:
            file.write((i + '\n'))

with open('directory_list.txt', 'r') as file_2:
    file_2.read()