from WoWMMORPG.WoWCharacters import Character
from random import randrange


class Mage(Character):
    def __init__(self, name, equipment, mana=100, attack_speed=2, delay=0):
        super().__init__(name, equipment, attack_speed, delay)
        self.max_mana = 100
        self.mana = mana
        self.attack_range = (8, 17)

    def end_round(self):
        super().end_round()
        if self.mana < 100:
            self.mana += 1
        else:
            self.mana = 100

    def lightning_spell(self):
        self.mana -= 55
        return randrange(30, 51)

    def attack(self):
        self.delay = self.max_delay - self.attack_speed
        if self.mana >= 55:
            self.lightning_spell()
        else:
            attack_damage = randrange(self.attack_range[0], self.attack_range[1]) * self.equipment.sword
            return round(attack_damage)