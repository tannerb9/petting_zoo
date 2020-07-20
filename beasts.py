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


class AirCreature(Creature):

    def __init__(self, name, species, food, chip_num, **shift):
        super().__init__(name, species, food, chip_num, **shift)
        self.flying = True

    def feed(self):
        print(
            f"{self.name} swooped through the air to catch the {self.food} for their meal on {date.today()}.")


class WaterCreature(Creature):

    def __init__(self, name, species, food, chip_num, **shift):
        super().__init__(name, species, food, chip_num, **shift)
        self.swimming = True

    def feed(self):
        print(f"{self.name} tossed their {self.food} into the air for fun before devouring it on {date.today()}.")


class LandCreature(Creature):

    def __init__(self, name, species, food, chip_num, **shift):
        super().__init__(name, species, food, chip_num, **shift)
        self.walking = True

    def feed(self):
        print(
            f"{self.name} frightened the {self.food} so they could chase it down on {date.today()}.")
