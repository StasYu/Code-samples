import zipfile
import string

zfile = zipfile.ZipFile('voyna-i-mir.zip', 'r')
name = zfile.namelist()
zfile.extractall()
zfile.close()

alpha = string.ascii_letters



def counter(name):
    file = open(name[0], 'r')
    result = dict()
    for i_line in file:
        for j_sym in i_line:
            if j_sym.isalpha():
                if j_sym not in result:
                    result[j_sym] = 0
                result[j_sym] += 1
    file.close()
    return result

let_dict = counter(name)

let_dict = dict(sorted(let_dict.items(), key= lambda x: x[1], reverse=True))

for i,j in let_dict.items():
    print(i,j)
