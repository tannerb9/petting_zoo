from datetime import date


class Creature:

    def __init__(self, name, species, food, chip_num, **shift):
        self.name = name
        self.shift = shift
        self.species = species
        self.date_added = date.today()
        self.food = food
        self.__chip_num = chip_num

        @property
        def chip_num(self):
            return self.__chip_num

        @chip_num.setter
        def chip_num(self, number):
            pass

    def feed(self):
        print(f"{self.name} was fed {self.food} on {date.today()}.")

    def __str__(self):
        return f"{self.name} is a {self.species}."
