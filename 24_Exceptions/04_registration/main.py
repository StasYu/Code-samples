# Иницииализировано три открытия друг в друге, так как не рекомендуется постоянно открывать и закрывать файлы в программе

with open('registrations.txt', 'r') as reg_file:
    with open('registrations_good.log', 'a') as good_file:
        with open('registrations_bad.log', 'a') as bad_file:

            for i_line in reg_file:
                temp_list = i_line.split()
                # print(temp_list)
                try:
                    if len(temp_list) != 3:
                        bad_file.write(' '.join(temp_list))
                        bad_file.write(' - IndexError')
                        bad_file.write('\n')
                        raise IndexError

                    if not temp_list[0].isalpha:
                        bad_file.write(' '.join(temp_list))
                        bad_file.write(' - NameError')
                        bad_file.write('\n')
                        raise NameError

                    if '@' not in temp_list[1] and '.' not in temp_list[1]:
                        bad_file.write(' '.join(temp_list))
                        bad_file.write(' - SyntaxError')
                        bad_file.write('\n')
                        raise SyntaxError

                    if not int(temp_list[2]) in range(10, 100):
                        bad_file.write(' '.join(temp_list))
                        bad_file.write(' - ValueError')
                        bad_file.write('\n')
                        raise ValueError

                except:
                    good_file.write(' '.join(temp_list))
                    good_file.write('\n')

# print(bad_file.closed)
# print(good_file.closed)
# print(reg_file.closed)