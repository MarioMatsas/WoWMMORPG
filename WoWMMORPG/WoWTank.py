from WoWMMORPG.WoWCharacters import Character


class Tank(Character):
    def __init__(self, name, equipment, attack_speed=2, delay=0):
        super().__init__(name, equipment, attack_speed, delay)
        self.attack_range = (20, 30)
        self.max_health = 2 * (100 * self.equipment.cape)
        self.health = 2 * (100 * self.equipment.cape)

