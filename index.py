from attractions import Attraction
from beasts import AirCreature, WaterCreature, LandCreature

aviary = Attraction("Aviary", "a cliff face to watch the beasts fly.")
woodlands = Attraction("Woodlands", "a tranquil forest where the beasts roam.")
seaside = Attraction("Seaside", "a glass submarine to see the sea creatures.")

vampy = AirCreature("Vampy", "vampire", "human", 1)
krakey = WaterCreature("Krakey", "kraken", "serpents", 2)
yetti = LandCreature("Yetti", "yeti", "snowcones", 3, shift="morning")
biggy = LandCreature("Biggy", "bigfoot", "bearclaws", 4, shift="morning")
basie = WaterCreature("Basie", "basilisk", "fish", 5)
draggy = AirCreature("Draggy", "dragon", "roasted humans", 6)
pterry = AirCreature("Pterry", "pterodactyl", "vermin", 7)
wolfy = LandCreature("Wolfy", "werewolf", "cow", 8, shift="night")
rexxy = LandCreature("Rexxy", "t-rex", "sheep", 9, shift="midday")
rapty = LandCreature("Rapty", "raptor", "deer", 10, shift="midday")
nessy = WaterCreature("Nessy", "loch ness monster", "fish", 11,)
meggy = WaterCreature("Meggy", "megalodon", "orca", 12)
zappy = AirCreature("Zappy", "zapdos", "berries", 13)
cthuly = WaterCreature("Cthuly", "cthulhu god", "souls of the damned", 14)
griffy = AirCreature("Griffy", "griffin", "vermin", 15)

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
