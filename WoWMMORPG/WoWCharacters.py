from random import randrange
from WoWEquipment import Equipment


class Character:
    def __init__(self, name, equipment, attack_speed=2, delay=0):
        self.name = name
        self.equipment = equipment
        self.max_delay = 5
        self.attack_range = (3, 11)
        self.max_health = 100 * self.equipment.cape
        self.health = 100 * self.equipment.cape
        self.attack_speed = attack_speed
        self.delay = delay

    def attack(self):
        attack_damage = randrange(self.attack_range[0], self.attack_range[1]) * self.equipment.sword
        self.delay = self.max_delay - self.attack_speed
        return round(attack_damage)

    def is_dead(self):
        return self.health <= 0

    def end_round(self):
        self.health = self.health + 1 if self.health + 1 < self.max_health else self.max_health
        if self.delay > 0:
            self.delay -= 1
        else:
            self.delay = 0

    def __str__(self):
        return f"| {self.name}'s stats |: H: {round(self.health)} -- ADelay: {self.delay}\n"

    def __repr__(self):
        return f'Character({self.name}, {self.attack_speed}, {self.delay}, {self.max_health}, {self.health}'

    def __iadd__(self, other):
        new_health = self.health + other
        return new_health

    def __isub__(self, other):
        new_health = self.health - other
        return new_health
