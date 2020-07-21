from datetime import date
from .creature import Creature
from movements.swimming import Swimming


class Kraken(Creature, Swimming):

    def __init__(self, name, species, food, chip_num, **shift):
        Creature.__init__(self, name, species, food, chip_num, **shift)
        Swimming.__init__(self)

    def feed(self):
        print(f"{self.name} tossed their {self.food} into the air for fun before devouring it on {date.today()}.")

    def __str__(self):
        return f"{self.name}, the {self.species}."
