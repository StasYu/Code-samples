import os

path = os.path.abspath(os.path.join('..'))
count_dictionary = {'file': 0, 'fold': 0, 'bite_size': 0}

def byt(path, dictionary=count_dictionary):
    stats = os.stat(path)
    dictionary['bite_size'] = (dictionary.get('bite_size') + (stats.st_size / 1024))
    return dictionary

def searcher(path, dictionary=count_dictionary):

    if os.path.isdir(path):
        byt(path)
        dictionary['fold'] = (dictionary.get('fold') + 1)

        for i_dir in os.listdir(path):
            new_path = os.path.abspath(os.path.join(path, i_dir))
            result = searcher(new_path)

    elif os.path.isfile(path):
        byt(path)
        dictionary['file'] = (dictionary.get('file') + 1)

        return path

    else:
        return None

count_search = searcher(path)
print(f"Размер каталога (в Кб): {count_dictionary['bite_size']}")
print(f"Количество подкаталогов: {count_dictionary['fold']}")
print(f"Количество файлов: {count_dictionary['file']}")