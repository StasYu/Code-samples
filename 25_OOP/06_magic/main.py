class Water:
    def __add__(self, new):
        if isinstance(new, Air):
            return Storm()
        elif isinstance(new, Fire):
            return Steam()
        elif isinstance(new, Earth):
            return Mud()

class Air:
    def __add__(self, new):
        if isinstance(new, Water):
            return Storm()
        elif isinstance(new, Fire):
            return Lightning()
        elif isinstance(new, Earth):
            return Dust()

class Fire:
    def __add__(self, new):
        if isinstance(new, Water):
            return Steam()
        elif isinstance(new, Air):
            return Lightning()
        elif isinstance(new, Earth):
            return Lava()

class Earth():
    def __add__(self, new):
        if isinstance(new, Water):
            return Mud()
        elif isinstance(new, Air):
            return Dust()
        elif isinstance(new, Fire):
            return Lava()


class Storm:
    new = 'Storm'

class Steam:
    new = 'Steam'

class Mud:
    new = 'Mud'

class Lightning:
    new = 'Lightning'

class Dust:
    new = 'Dust'

class Lava:
    new = 'Lava'


water = Water()
fire = Fire()
air = Air()
earth = Earth()
combo_1 = water + fire
combo_2 = water + air
combo_3 = water + earth
combo_4 = water + air
combo_5 = fire + air
combo_6 = earth + fire

print(combo_1.new, combo_2.new, combo_5.new)