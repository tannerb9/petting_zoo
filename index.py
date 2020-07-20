from attractions import Attraction
from beasts import Creature

aviary = Attraction("Aviary", "a cliff face to watch the beasts fly.")
woodlands = Attraction("Woodlands", "a tranquil forest where the beasts roam.")
seaside = Attraction("Seaside", "a glass submarine to see the sea creatures.")

vampy = Creature("Vampy", "vampire", "blood", 1)
krakey = Creature("Krakey", "kraken", "serpents", 2)
yetti = Creature("Yetti", "yeti", "snowcones", 3, shift="morning")
biggy = Creature("Biggy", "bigfoot", "bearclaws", 4, shift="morning")
basie = Creature("Basie", "basilisk", "critters", 5)
draggy = Creature("Draggy", "dragon", "roasted humans", 6)
pterry = Creature("Pterry", "pterodactyl", "vermin", 7)
wolfy = Creature("Wolfy", "werewolf", "raw beef", 8, shift="night")
rexxy = Creature("Rexxy", "t-rex", "sheep", 9, shift="midday")
rapty = Creature("Rapty", "raptor", "deer", 10, shift="midday")
nessy = Creature("Nessy", "loch ness monster", "fish", 11,)
meggy = Creature("Meggy", "megalodon", "orca", 12)
zappy = Creature("Zappy", "zapdos", "berries", 13)
cthuly = Creature("Cthuly", "cthulhu god", "souls of the damned", 14)
griffy = Creature("Griffy", "griffin", "vermin", 15)

print(
    f"{rexxy.name} the {rexxy.species} is available to pet during the {rexxy.shift['shift']} shift.")
griffy.feed()
rexxy.feed()

aviary.addAnimals(pterry, draggy, zappy, griffy, vampy)
woodlands.addAnimals(yetti, biggy, wolfy, rexxy, rapty)
seaside.addAnimals(cthuly, meggy, nessy, basie, krakey)

print(f"The {aviary.name} is where you'll find creatures that roam the skies, like")
for creature in aviary.animals:
    print(f"    * {creature}")

print(f"The {woodlands.name} is where you'll find creatures that lurk in the woods, like")
for creature in woodlands.animals:
    print(f"    * {creature}")

print(f"The {seaside.name} is where you'll find creatures that reside in the depths, like")
for creature in seaside.animals:
    print(f"    * {creature}")

print(aviary.last_creature_added)
