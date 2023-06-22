alphabet = [
    'а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з',
    'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р',
    'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ',
    'ъ', 'ы', 'ь', 'э', 'ю', 'я'
]
# print(len(alphabet))
# print(alphabet.index('э'))

def index_msg(alphabet, i_msg, step):
    if alphabet.index(i_msg) > len(alphabet) - 1 - step:
        new_ind = alphabet.index(i_msg) + step - 33
    else:
        new_ind = alphabet.index(i_msg) + step
    return(alphabet[new_ind])

msg = input('Введите сообщение: ')
step = int(input('Введите сдвиг: '))

new_msg = [' ' if i_msg == ' ' else index_msg(alphabet, i_msg, step) for i_msg in msg]
for i in new_msg:
    print(i, end='')