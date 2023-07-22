zen_file = open('zen.txt', 'r')
new_file = open('new_zen', 'a')

for i in zen_file:
    new_file.write(i)

new_file.close()
new_file = open('new_zen', 'r')

print(new_file.read())