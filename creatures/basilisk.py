from creatures.creature import WaterCreature


class Basilisk(WaterCreature):

    def __init__(self, name, species, food, chip_num, **shift):
        super().__init__(name, species, food, chip_num, **shift)
