from WoWCharacters import Character
from WoWArena import Arena
from WoWEquipment import Equipment
from random import uniform, randrange
from WoWMage import Mage
from WoWTank import Tank


def main():
    orcs = [Character(f'Orc {i}', Equipment(uniform(1.1, 1.5), uniform(1.1, 1.3)), 2, randrange(4)) for i in range(1, 5)]
    orcs += [Tank('Tank Orc', Equipment(uniform(1.1, 1.5), uniform(1.1, 1.3)), 2, randrange(4))]

    elves = [Character(f'Night-Elf {i}', Equipment(uniform(1.1, 1.5), uniform(1.1, 1.3)), 3, randrange(3)) for i in range(1, 5)]
    elves += [Mage('Mage Night-Elf', Equipment(uniform(1.1, 1.5), uniform(1.1, 1.3)), 4, randrange(3))]

    a = Arena(orcs, elves)
    a.play()


main()