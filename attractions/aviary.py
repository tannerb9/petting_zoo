from attractions.attraction import Attraction


class Aviary(Attraction):

    def __init__(self, name, description):
        super().__init__(name, description)

    def add_creature_type_check(self, creature):
        try:
            if creature.flight_speed > -1:
                self.animals.append(creature)
        except AttributeError as ex:
            print(
                f"{creature.name} isn't suited for the aviary, so please don't put them in the {self.name} attraction.")
