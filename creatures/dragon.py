from datetime import date
from .creature import Creature
from movements.flying import Flying


class Dragon(Creature, Flying):

    def __init__(self, name, species, food, chip_num, **shift):
        Creature.__init__(self, name, species, food, chip_num, **shift)
        Flying.__init__(self)

    def feed(self):
        print(
            f"{self.name} swooped through the air to catch the {self.food} for their meal on {date.today()}.")

    def __str__(self):
        return f"{self.name}, the {self.species}."
