from datetime import date


class Griffin:

    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.flying = True


class Yeti:

    def __init__(self, name, species, shift):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.shift = shift
        self.walking = True


class Bigfoot:

    def __init__(self, name, species, shift):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.shift = shift
        self.walking = True


class T_Rex:

    def __init__(self, name, species, shift):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.shift = shift
        self.walking = True


class Raptor:

    def __init__(self, name, species, shift):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.shift = shift
        self.walking = True


class Cthulhu:

    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True


class Zapdos:

    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.flying = True


class Pterodactyl:

    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.flying = True


class Megalodon:

    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True


class Loch_Ness:

    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True


class Werewolf:

    def __init__(self, name, species, shift):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.shift = shift
        self.walking = True


class Vampire:

    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.flying = True


class Dragon:

    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.flying = True


class Basilisk:

    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True


class Kraken:

    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True


vampy = Vampire("Vampy", "hybrid")
krakey = Kraken("Krakey", "squid")
yetti = Yeti("Yetti", "unknown", "morning")
biggy = Bigfoot("Biggy", "unknown", "morning")
basie = Basilisk("Basie", "serpent")
draggy = Dragon("Draggy", "serpent")
pterry = Pterodactyl("Pterry", "dinosaur")
wolfy = Werewolf("Wolfy", "canine", "night")
rexxy = T_Rex("Rexxy", "dinosaur", "midday")
rapty = Raptor("Rapty", "dinosaur", "midday")
nessy = Loch_Ness("Nessy", "serpent")
meggy = Megalodon("Meggy", "shark")
zappy = Zapdos("Zappy", "bird")
cthuly = Cthulhu("Cthuly", "hybrid")
griffy = Griffin("Griffy", "hybrid")

print(f"{rexxy.name} the {rexxy.species} is available to pet during the {rexxy.shift} shift.")
