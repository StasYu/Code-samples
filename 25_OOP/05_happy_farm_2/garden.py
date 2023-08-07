class Potato:
    states = {0: 'None', 1: 'Shoot', 2: 'Green', 3: 'Ripe'}

    def __init__(self, index):
        self.p_index = index
        self.stage = 0

    def grow(self):
        if self.stage < 3:
            self.stage += 1
        # self.potato_grow_info()

    def is_grow(self):
        if self.stage == 3:
            return True
        return False

    def potato_grow_info(self):
        print(f'Potato number {self.p_index} is {self.states[self.stage]}')

class PotatoGarden:

    def __init__(self, index):
        self.potato_list = [Potato(index) for index in range(1, index + 1)]

    def all_grow(self):
        for i_potato in self.potato_list:
            i_potato.grow()

    def is_all_grow(self):
        if all([i_potato.is_grow() for i_potato in self.potato_list]):
            print('\nAll potatoes is grew up enough\n')
            return True
        else:
            print('\nPotatoes is not ripe yet\n')
            return False

class Gardener:

    def __init__(self, garden, name='Alfred'):
        self.name = name
        self.garden = garden
        self.crop = list()

    def care_garden(self):
        self.garden.all_grow()
        self.harvest()

    def harvest(self):
        print('\nharvesting...')
        for i_potato in self.garden.potato_list:
            if i_potato.is_grow():
                self.crop.append(i_potato.p_index)
                i_potato.stage = 0
            else:
                print(f'potato {i_potato.p_index} is not grow enough')
        print(f'\nour crop today is: {self.crop}\n')
        self.crop = list()


