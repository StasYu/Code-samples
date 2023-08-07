from random import randint

class KillError(Exception):
    pass

class DrunkError(Exception):
    pass

class CarCrashError(Exception):
    pass

class GluttonyError(Exception):
    pass

class DepressionError(Exception):
    pass


class Life():
    __carma = 0

    def one_day(self):
        carma = randint(1, 7)
        coin = randint(1, 10)
        maybe = randint(1, 5)

        if coin == 10:
            with open('karma.log', 'a') as sins:
                try:
                    if maybe == 1:
                        raise KillError
                    elif maybe == 2:
                        raise DrunkError
                    elif maybe == 3:
                        raise CarCrashError
                    elif maybe == 4:
                        raise GluttonyError
                    elif maybe == 5:
                        raise DepressionError
                except KillError:
                    sins.write('KillError\n')
                except DrunkError:
                    sins.write('DrunkError\n')
                except CarCrashError:
                    sins.write('CarCrashError\n')
                except GluttonyError:
                    sins.write('GluttonyError\n')
                except DepressionError:
                    sins.write('DepressionError\n')

        else:
            self.__carma += carma
            if self.__carma > 500:
                self.__carma = 500
                print(self.__carma)
            return carma

    def get_carma(self):
        return self.__carma

life = Life()

with open('karma.log', 'w'):
    while life.get_carma() != 500:
        life.one_day()

print('You are reached Nirvana')