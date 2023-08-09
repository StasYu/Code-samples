class Stack:
    def __init__(self):
        self.__tasks = list()

    def get_task(self):
        return self.__tasks

    def add_elem(self, elem):
        self.__tasks.append(elem)

    def pop_elem(self):
        self.__tasks.pop()

class TaskManager():

    def __init__(self):
        self.__tm = dict()

    def __str__(self):
        output = list()
        if self.__tm:
            for i_prior in sorted(self.__tm.keys()):
                temp = '; '.join(self.__tm[i_prior].get_task())
                output.append(f'{i_prior} {temp}\n')

        return ''.join(output)

    def new_task(self, task, prior):
        if prior not in self.__tm:
            self.__tm[prior] = Stack()
        self.__tm[prior].add_elem(task)

manager = TaskManager()
manager.new_task(task="сделать уборку", prior=4)
manager.new_task(task="помыть посуду", prior=4)
manager.new_task(task="отдохнуть", prior=1)
manager.new_task(task="поесть", prior=2)
manager.new_task(task="сдать дз", prior=2)
print(manager)
