class Attraction:

    def __init__(self, name, description):
        self.name = name
        self.animals = []

    def addAnimals(self, *animals):
        for animal in animals:
            self.animals.append(animal)


# class Seaside:

#     def __init__(self, name, description):
#         self.name = name
#         self.animals = []

#     def addAnimals(self, *animals):
#         for animal in animals:
#             self.animals.append(animal)


# class Woodlands:

#     def __init__(self, name, description):
#         self.name = name
#         self.animals = []

#     def addAnimals(self, *animals):
#         for animal in animals:
#             self.animals.append(animal)
