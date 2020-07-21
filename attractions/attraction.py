class Attraction:

    def __init__(self, name, description):
        self.name = name
        self.animals = []

    def add_animals(self, *animals):
        for animal in animals:
            self.animals.append(animal)

    def remove_animal(self, animal):
        self.animals.remove(animal)

    def __str__(self):
        return f"{self.name} ({len(self)} animals)"

    def __len__(self):
        return len(self.animals)

    @property
    def last_creature_added(self):
        return self.animals[-1]
