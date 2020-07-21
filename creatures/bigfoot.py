from creatures.creature import LandCreature


class Bigfoot(LandCreature):

    def __init__(self, name, species, food, chip_num, **shift):
        super().__init__(name, species, food, chip_num, **shift)
