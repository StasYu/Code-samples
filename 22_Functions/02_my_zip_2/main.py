# data_string = '1234'
# data_dict = {1:'a', 2:'a', 'b':3, 'c': 4}

# data_tuple = ('a','b','c')
# data_int = 1
# data_list = ['a', 'b', 'c']
#

first = 'abcde'
# second = {1:'a', 2:'a', 'b':3, 'c': 4}

second = 1,2,3,4,5,6
def minimal_len(first, second):
    return(min(len(first), len(second)))

def dats(val):
    temp = [i for i in val]
    return temp

def pair (first, second, length):
    temp = ((dats(first)[i], dats(second)[i]) for i in range(length))
    return temp

min_len = minimal_len(first, second)
zipped = pair(first, second, min_len)

print(zipped)
for i in zipped:
    print(i)