class Parent:
    def __init__(self, child, name='', age=0):
        self.name = name

        if age <= age - child.age:
            print('Your kid is too old')
        else:
            self.age = age

        self.child = child

    def info(self):
        print(f'Name: {self.name}, age: {self.age}, Kid: {self.child.name}\n')

    def parent_care(self):
        self.time_to_feed()
        self.time_to_calm()

    def time_to_feed(self):
        state = self.child.hunger_list[self.child.is_hungry]
        print(f'{self.child.name} is {state}')
        if self.child.is_hungry == 2:
            print('Feeding a child\n')
            self.child.is_hungry = 0

    def time_to_calm(self):
        state = self.child.calm_list[self.child.is_calm]
        print(f'{self.child.name} is {state}')
        if self.child.is_calm == 2:
            print('Playing with child\n')
            self.child.is_calm = 0

class Child:
    hunger_list = {0: 'Overate', 1: 'Satisfied', 2: 'Starve'}
    calm_list = {0: 'Calm', 1: 'Excited', 2: 'at Scandal'}
    def __init__(self, name='', age=0):
        self.name = name
        self.age = age
        self.is_calm = 0
        self.is_hungry = 0

    def hunger_change(self):
        if self.is_hungry < 2:
            self.is_hungry += 1
        else:
            print(f'\n{self.name} is hungry, time to eat!')

    def state_change(self):
        if self.is_calm < 2:
            self.is_calm += 1
        else:
            print(f'\n{self.name} is at rage, need to calm')



kid_1 = Child('Bob', 2)
parent_1 = Parent(kid_1, 'Sam', 32)
parent_1.info()

print('Checking kid state\n')
parent_1.parent_care()

print('\nA few hours later')
kid_1.hunger_change()
kid_1.state_change()

print('\nA few hours later')
kid_1.hunger_change()
kid_1.state_change()

print('\nA few hours later')
kid_1.hunger_change()
kid_1.state_change()

print('Checking kid state\n')
parent_1.parent_care()
print('Checking kid state\n')
parent_1.parent_care()