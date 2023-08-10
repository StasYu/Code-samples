class Property:
    def __init__(self, name):
        self.__name = name
        self.__money = int(input(f'\n{self.__name:}\n'
                                 f'Input ur budget: '))
        self.__worth = int(input('Input property value: '))
        self.__tax = self.tax_calc()

    def tax_calc(self):
        pass

    def get_worth(self):
        return int(self.__worth)

    def get_money(self):
        return int(self.__money)

    def info(self):
        print(f'\n{self.__name}'
              f'\nYour funds: {self.get_money()}\n'
              f'Cost: {self.get_worth()}\n'
              f'tax: {self.tax_calc()}')

class Appartment(Property):
    def __init__(self, name):
        super().__init__(name)
        self.__tax = self.tax_calc()

    def tax_calc(self):
        tax = self.get_worth() / 1000
        return tax

    def is_enough(self):
        self.info()
        if self.get_money() < self.get_worth() + self.tax_calc():
            gap = round(self.get_worth() + self.tax_calc() - self.get_money(), 2)
            print(f'Not enough money. needed {gap} more')
        else:
            gap = round(self.get_money() - self.get_worth() - self.tax_calc())
            print(f'You can buy appartment. remain {gap}')

class Car(Property):
    def __init__(self, name):
        super().__init__(name)
        self.__tax = self.tax_calc()

    def tax_calc(self):
        tax = self.get_worth() / 200
        return tax

    def is_enough(self):
        self.info()
        if self.get_money() < self.get_worth() + self.tax_calc():
            gap = round(self.get_worth() + self.tax_calc() - self.get_money(), 2)
            print(f'Not enough money. needed {gap} more')
        else:
            gap = round(self.get_money() - self.get_worth() - self.tax_calc())
            print(f'You can buy appartment. remain {gap}')

class CountryHouse(Property):

    def __init__(self, name):
        super().__init__(name)
        self.__tax = self.tax_calc()

    def tax_calc(self):
        tax = self.get_worth() / 500
        return tax

    def is_enough(self):
        self.info()
        if self.get_money() < self.get_worth() + self.tax_calc():
            gap = round(self.get_worth() + self.tax_calc() - self.get_money(), 2)
            print(f'Not enough money. needed {gap} more')
        else:
            gap = round(self.get_money() - self.get_worth() - self.tax_calc())
            print(f'You can buy appartment. remain {gap}')


appartment = Appartment('Appartment')
car = Car('Toyota')
country_house = CountryHouse('Dacha')
appartment.is_enough()
car.is_enough()
country_house.is_enough()