text = list(input('Сообщение: '))
new_msg = []
temp = []

for i in text:
    if i.isalpha():
        temp.insert(0, i)
    else:
        ''.join(temp)
        new_msg.extend(temp)
        new_msg.append(i)
        temp = []

print('Новое сообщение: ', ''.join(new_msg))
