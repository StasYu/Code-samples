
class QHofstadter:

    def __init__(self, subseq: list, limit: int) -> None:
        if subseq == [1, 2]:
            raise ValueError
        else:
            self.__s = subseq

        self.__limit = limit
        self.__counter = 0

    def __next__(self) -> int:

        self.__counter += 1
        if self.__counter < self.__limit + 1:
            try:
                result = self.__s[-self.__s[-1]] + self.__s[-self.__s[-2]]
                self.__s.append(result)
            except IndexError:
                raise StopIteration
            return result
        else:
            raise StopIteration

    def q_list(self) -> list:
        return self.__s

    def __iter__(self) -> 'QHofstadter':
        self.counter = 0
        return self


q_hoff = QHofstadter(([1, 1]), 10)

for i_num in q_hoff:
    continue

print(q_hoff.q_list())