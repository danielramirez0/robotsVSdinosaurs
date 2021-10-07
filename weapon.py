class Weapon:
    def __init__(self, name: str, attack_power: int):
        self.name = name
        self.attack_power = attack_power
        self.is_equipped = False