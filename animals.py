from datetime import date


class Griffin:

    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.flying = True


class Yeti:

    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True


class Bigfoot:

    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True


class T_Rex:

    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True


class Raptor:

    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
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

    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
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


vampy = Vampire("vampy", "hybrid")
krakey = Kraken("krakey", "squid")
yetti = Yeti("yetti", "unknown")
biggy = Bigfoot("biggy", "unknown")
basie = Basilisk("basie", "serpent")
draggy = Dragon("draggy", "serpent")
pterry = Pterodactyl("pterry", "dinosaur")
wolfy = Werewolf("wolfy", "canine")
rexxy = T_Rex("rexxy", "dinosaur")
rapty = Raptor("rapty", "dinosaur")
nessy = Loch_Ness("nessy", "serpent")
meggy = Megalodon("meggy", "shark")
zappy = Zapdos("zappy", "bird")
cthuly = Cthulhu("cthuly", "hybrid")
griffy = Griffin("griffy", "hybrid")

print(rexxy)
