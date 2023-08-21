import os
from collections import Iterable

class Gener:

    def __init__(self, file: str):
        self.__path = file
        self.__file_dir = os.listdir(self.__path)
        self.__counter = 0
        self.__line_num = 0

    def __iter__(self) -> Iterable:
        self.counter = 0
        self.__line_num = 0
        return self

    def get_counter(self) -> int:
        return self.__counter

    def __next__(self) -> int:
        if self.__counter < len(self.__file_dir):
            self.__i = self.__file_dir[self.__counter]
            self.__counter += 1
            if self.__i.endswith('.py'):
                self.count()
                return self.get_line_num()
        else:
            raise StopIteration
        return self.get_line_num()


    def count(self):
        new_path = os.path.join(self.__path, self.__i)
        with open(new_path, 'r') as file:
            for i_line in file:
                if not len(i_line) == 0 and not i_line == '\n':
                    if not i_line.startswith('#'):
                        self.__line_num += 1

    def get_line_num(self) -> int:
        return self.__line_num


file_path = os.path.abspath(os.path.join(''))
file_dir = os.listdir(file_path)

new = Gener(file_path)
for i in new:
    continue
print(new.get_line_num())