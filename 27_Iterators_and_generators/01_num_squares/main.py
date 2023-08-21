from collections.abc import Iterable

class MyIter:
    def __init__(self, limit: int) -> None:
        self.__limit = limit
        self.__num = 0
        self.__counter = 0

    def __iter__(self) -> 'MyIter':
        self.__num = 0
        self.__counter = 0
        return self

    def __next__(self) -> int:
        self.__counter += 1
        if self.__counter > self.__limit:
            raise StopIteration
        self.__num = self.__counter ** 2
        return self.__num
# ----------------------------------------------------
def my_gener(limit: int) -> int:
    counter = 1
    while counter <= limit:
        temp = counter ** 2
        yield temp
        counter += 1

# ----------------------------------------------------
num = int(input('Введите число: '))
# ----------------------------------------------------
my_gen_2 = (i**2 for i in range(1, num+1))
# ____________________________________________________
my_iter = MyIter(num)
my_gen = my_gener(num)
# -----------------------------------------------------
for i in my_iter:
    print(i)
print()

for i in my_gen:
    print(i)
print()

for i in my_gen_2:
    print(i)
