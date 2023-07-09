# string = 'aabcaa' #not palin delete later
# string = 'aaabbcc' #palin delete later

string = input('Введите строку: ')
string_dict = {i: string.count(i) % 2 for i in set(string)}

if len(string) % 2 == 0 and 1 in string_dict.values():
    print('Нельзя сделать палиндромом')
elif len(string) % 2 != 0 and sum(string_dict.values()) != 1:
    print('Нельзя сделать палиндромом')
else:
    print('Можно сделать палиндромом')

