from creatures.creature import AirCreature


class Dragon(AirCreature):

    def __init__(self, name, species, food, chip_num, **shift):
        super().__init__(name, species, food, chip_num, **shift)
