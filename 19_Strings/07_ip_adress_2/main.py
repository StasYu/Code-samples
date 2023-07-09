while True:
    address = input('\nВведите IP: ')
    address_lst = address.split('.')
    # print(address_lst)
    flag = False

    for i in address_lst:
        if i.isalnum() and not i.isdigit():
            print(i, ' - не целое число')
            flag = False
            break

        elif not i.isdigit() and not i.isalnum():
            print('Адрес - это четыре числа, разделенные точками')
            flag = False
            break

        elif not int(i) <= 255:
            print(i, 'превышает 255')
            flag = False
            break

        else:
            flag = True

    if flag:
        print('\nIP-адрес корректен')
        break