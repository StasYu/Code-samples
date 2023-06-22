string = ['a', 'b', 'h', 'e', 'b', 'r', 'y', 't', 'h']
def num(i):
    if i == True:
        return()
count_list = [i_num for i_num in range(len(string)) if string[i_num] == 'h']
print(string[count_list[0] + 1:count_list[1]])