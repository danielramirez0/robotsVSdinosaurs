class Weapon:
    def __init__(self, name: str, attack_power: int, cost):
        self.name = name
        self.attack_power = attack_power
        self.cost = cost
        self.is_equipped = False
