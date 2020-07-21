from datetime import date
from .creature import Creature
from movements.walking import Walking


class Werewolf(Creature, Walking):

    def __init__(self, name, species, food, chip_num, **shift):
        Creature.__init__(self, name, species, food, chip_num, **shift)
        Walking.__init__(self)

    def feed(self):
        print(
            f"{self.name} frightened the {self.food} so they could chase it down on {date.today()}.")

    def __str__(self):
        return f"{self.name}, the {self.species}."
