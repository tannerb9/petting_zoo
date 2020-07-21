from attractions import Aviary, Seaside, Woodlands
from creatures import Basilisk
from creatures import Bigfoot
from creatures import Cthulhu
from creatures import Dragon
from creatures import Griffin
from creatures import Kraken
from creatures import Loch_Ness
from creatures import Megalodon
from creatures import Pterodactyl
from creatures import Raptor
from creatures import T_Rex
from creatures import Vampire
from creatures import Werewolf
from creatures import Yeti
from creatures import Zapdos

aviary = Aviary("Aviary", "a cliff face to watch the beasts fly.")
woodlands = Woodlands("Woodlands", "a tranquil forest where the beasts roam.")
seaside = Seaside("Seaside", "a glass submarine to see the sea creatures.")

vampy = Vampire("Vampy", "vampire", "human", 1)
krakey = Kraken("Krakey", "kraken", "serpents", 2)
yetti = Yeti("Yetti", "yeti", "snowcones", 3, shift="morning")
biggy = Bigfoot("Biggy", "bigfoot", "bearclaws", 4, shift="morning")
basie = Basilisk("Basie", "basilisk", "fish", 5)
draggy = Dragon("Draggy", "dragon", "roasted humans", 6)
pterry = Pterodactyl("Pterry", "pterodactyl", "vermin", 7)
wolfy = Werewolf("Wolfy", "werewolf", "cow", 8, shift="night")
rexxy = T_Rex("Rexxy", "t-rex", "sheep", 9, shift="midday")
rapty = Raptor("Rapty", "raptor", "deer", 10, shift="midday")
nessy = Loch_Ness("Nessy", "loch ness monster", "fish", 11,)
meggy = Megalodon("Meggy", "megalodon", "orca", 12)
zappy = Zapdos("Zappy", "zapdos", "berries", 13)
cthuly = Cthulhu("Cthuly", "cthulhu god", "souls of the damned", 14)
griffy = Griffin("Griffy", "griffin", "vermin", 15)

print(
    f"{rexxy.name} the {rexxy.species} is available to pet during the {rexxy.shift['shift']} shift.")
griffy.feed()
rexxy.feed()

aviary.add_animals(pterry, draggy, zappy, griffy, vampy)
woodlands.add_animals(yetti, biggy, wolfy, rexxy, rapty)
seaside.add_animals(cthuly, meggy, nessy, basie, krakey)

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
woodlands.add_creature_type_check(nessy)
aviary.add_creature_type_check(biggy)
seaside.add_creature_type_check(rapty)
