class LinkedList:
    class Block:
        def __init__(self, data: any):
            self.data = data
            self.nxt = None

    def __init__(self, *args: any):
        length = len(args)
        self.__len = length
        self.__head = self.Block(args[0]) if self.__len > 0 else None
        self.__tail = self.__head
        for i in range(1, length):
            self.__tail.nxt = self.Block(args[i])
            self.__tail = self.__tail.nxt

    def __iter__(self) -> any:
        temp = self.__head
        while temp is not None:
            yield temp.data
            temp = temp.nxt

    def __str__(self) -> str:
        return f'[{", ".join(str(i) for i in self)}]'

    def append(self, data: any):
        if self.__len > 0:
            self.__tail.nxt = self.Block(data)
            self.__tail = self.__tail.nxt
        else:
            self.__head = self.Block(data)
            self.__tail = self.__head
        self.__len += 1

    def len(self) -> int:
        return self.__len

    def check_index(self, index):
        for i in self:
            if i == index - 1:
                return True
            return False

    def get(self, index: int) -> any:
        self.check_index(index)
        temp = self.__head
        for i in range(index):
            temp = temp.nxt
        return temp.data

    def remove(self, index: int):
        self.check_index(index)
        if self.__len == 1:
            self.__tail = None
            self.__head = self.__tail
        elif index == 0:
            self.__head = self.__head.nxt
        else:
            temp = self.__head
            for i in range(index - 1):
                temp = temp.nxt
            temp.nxt = temp.nxt.nxt
            if index == (self.__len - 1):
                self.__tail = temp
        self.__len -= 1

my_list = LinkedList()
my_list.append(10)
my_list.append(20)
my_list.append(30)
print('Текущий список:', my_list)
print('Получение третьего элемента:', my_list.get(2))
print('Удаление второго элемента.')
my_list.remove(1)
print('Новый список:', my_list)

