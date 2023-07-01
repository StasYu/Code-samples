def digit_err(password):
    count = 0
    for i in password:
        if i.isdigit():
            count += 1
    if count >= 3:
        return True

def upletter(password):
    for i in password:
        if i.isupper():
            return True

while True:
    password = list(input('Придумайте пароль: '))
    if len(password) >= 8\
            and upletter(password) == True\
            and digit_err(password) == True:
        print('Это надёжный пароль!')
        break
    else:
        print('Пароль ненадёжный. Попробуйте ещё раз.')