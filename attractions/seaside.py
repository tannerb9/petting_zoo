from attractions.attraction import Attraction


class Seaside(Attraction):

    def __init__(self, name, description):
        super().__init__(name, description)

    def add_creature_type_check(self, creature):
        try:
            if creature.swim_speed > -1:
                self.animals.append(creature)
        except AttributeError as ex:
            print(
                f"{creature.name} doesn't like the water, so don't put them in the {self.name} attraction.")
