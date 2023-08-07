from garden import PotatoGarden, Gardener
from random import randint


index = int(input('Enter q-ty of potatoes: '))
print()
new_garden = PotatoGarden(index)
new_gardener = Gardener(new_garden, 'Tom')

for i in range(10):
    if i == 1 or i == 5 or i == 8:
        r_index = randint(1, index + 1)
        new_garden.potato_list[r_index].stage -= 1
        r_index = randint(1, index + 1)
        new_garden.potato_list[r_index].stage -= 2
    new_gardener.care_garden()
