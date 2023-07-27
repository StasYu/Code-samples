import string
import os

alph = string.ascii_lowercase
step = 0
path = os.path.abspath(os.path.join('text.txt'))
new_path = os.path.abspath(os.path.join('cipher_text.txt'))

def cipher(text, step, alpha=alph):
    new_text = str()
    for i_let in text.lower():
        if i_let in alph:
            pos = alpha.find(i_let)
            if pos + step < len(alpha):
                new_pos = pos + step
            else:
                new_pos = (pos + step) % (len(alpha))
            new_text += alph[new_pos]
        else:
            new_text += i_let
    return new_text


new_file = open(new_path, 'w')
new_file.write('')
new_file.close()

file = open(path, 'r')
new_file = open(new_path, 'a')

for i_line in file:
    step += 1
    new_text = cipher(i_line, step)
    new_file.write(new_text)

file.close()
new_file.close()

new_file = open(new_path, 'r')
print(new_file.read())
new_file.close