from datetime import date


class Creature:

    def __init__(self, name, species, food, **shift):
        self.name = name
        self.shift = shift
        self.species = species
        self.date_added = date.today()
        self.food = food

    def feed(self):
        print(f"{self.name} was fed {self.food} on {date.today()}.")

    def __str__(self):
        return f"{self.name} is a {self.species}."
