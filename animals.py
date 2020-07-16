from datetime import date
from datetime import datetime


class Griffin:

    def __init__(self, name, species, food):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.flying = True
        self.food = food

    def feed(self):
        print(f"{self.name} was fed {self.food} on {date.today()}.")

    def __str__(self):
        return f"{self.name} is a {self.species}."


class Yeti:

    def __init__(self, name, species, food, shift):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.shift = shift
        self.walking = True
        self.food = food

    def feed(self):
        print(f"{self.name} was fed {self.food} on {date.today()}.")

    def __str__(self):
        return f"{self.name} is a {self.species}."


class Bigfoot:

    def __init__(self, name, species, food, shift):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.shift = shift
        self.walking = True
        self.food = food

    def feed(self):
        print(f"{self.name} was fed {self.food} on {date.today()}.")

    def __str__(self):
        return f"{self.name} is a {self.species}."


class T_Rex:

    def __init__(self, name, species, food, shift):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.shift = shift
        self.walking = True
        self.food = food

    def feed(self):
        print(f"{self.name} was fed {self.food} on {date.today()}.")

    def __str__(self):
        return f"{self.name} is a {self.species}."


class Raptor:

    def __init__(self, name, species, food, shift):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.shift = shift
        self.walking = True
        self.food = food

    def feed(self):
        print(f"{self.name} was fed {self.food} on {date.today()}.")

    def __str__(self):
        return f"{self.name} is a {self.species}."


class Cthulhu:

    def __init__(self, name, species, food):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True
        self.food = food

    def feed(self):
        print(f"{self.name} was fed {self.food} on {date.today()}.")

    def __str__(self):
        return f"{self.name} is a {self.species}."


class Zapdos:

    def __init__(self, name, species, food):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.flying = True
        self.food = food

    def feed(self):
        print(f"{self.name} was fed {self.food} on {date.today()}.")

    def __str__(self):
        return f"{self.name} is a {self.species}."


class Pterodactyl:

    def __init__(self, name, species, food):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.flying = True
        self.food = food

    def feed(self):
        print(f"{self.name} was fed {self.food} on {date.today()}.")

    def __str__(self):
        return f"{self.name} is a {self.species}."


class Megalodon:

    def __init__(self, name, species, food):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True
        self.food = food

    def feed(self):
        print(f"{self.name} was fed {self.food} on {date.today()}.")

    def __str__(self):
        return f"{self.name} is a {self.species}."


class Loch_Ness:

    def __init__(self, name, species, food):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True
        self.food = food

    def feed(self):
        print(f"{self.name} was fed {self.food} on {date.today()}.")

    def __str__(self):
        return f"{self.name} is a {self.species}."


class Werewolf:

    def __init__(self, name, species, food, shift):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.shift = shift
        self.walking = True
        self.food = food

    def feed(self):
        print(f"{self.name} was fed {self.food} on {date.today()}.")

    def __str__(self):
        return f"{self.name} is a {self.species}."


class Vampire:

    def __init__(self, name, species, food):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.flying = True
        self.food = food

    def feed(self):
        print(f"{self.name} was fed {self.food} on {date.today()}.")

    def __str__(self):
        return f"{self.name} is a {self.species}."


class Dragon:

    def __init__(self, name, species, food):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.flying = True
        self.food = food

    def feed(self):
        print(f"{self.name} was fed {self.food} on {date.today()}.")

    def __str__(self):
        return f"{self.name} is a {self.species}."


class Basilisk:

    def __init__(self, name, species, food):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True
        self.food = food

    def feed(self):
        print(f"{self.name} was fed {self.food} on {date.today()}.")

    def __str__(self):
        return f"{self.name} is a {self.species}."


class Kraken:

    def __init__(self, name, species, food):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True
        self.food = food

    def feed(self):
        print(f"{self.name} was fed {self.food} on {date.today()}.")

    def __str__(self):
        return f"{self.name} is a {self.species}."


vampy = Vampire("Vampy", "hybrid", "blood")
krakey = Kraken("Krakey", "squid", "serpents")
yetti = Yeti("Yetti", "unknown", "snowcones", "morning")
biggy = Bigfoot("Biggy", "unknown", "bearclaws", "morning")
basie = Basilisk("Basie", "serpent", "critters")
draggy = Dragon("Draggy", "serpent", "roasted humans")
pterry = Pterodactyl("Pterry", "dinosaur", "vermin")
wolfy = Werewolf("Wolfy", "canine", "raw beef", "night")
rexxy = T_Rex("Rexxy", "dinosaur", "sheep", "midday")
rapty = Raptor("Rapty", "dinosaur", "deer", "midday")
nessy = Loch_Ness("Nessy", "serpent", "fish")
meggy = Megalodon("Meggy", "shark", "orca")
zappy = Zapdos("Zappy", "bird", "berries")
cthuly = Cthulhu("Cthuly", "hybrid", "souls of the damned")
griffy = Griffin("Griffy", "hybrid", "vermin")

print(f"{rexxy.name} the {rexxy.species} is available to pet during the {rexxy.shift} shift.")
griffy.feed()
rexxy.feed()
print(cthuly)
