tup_string = (1,2,3,4,5,2,6)
number = input('enter symbol: ')

if number.isdigit():
    number = int(number)

if number in tup_string:
    if number not in tup_string[tup_string.index(number) + 1:]:
        print(tup_string[tup_string.index(number):])
    else:
        index = tup_string.index(number, tup_string.index(number) + 1)
        print(tup_string[tup_string.index(number):index + 1])
else:
    print(())

# print(tup_string[tup_string.index(number):])