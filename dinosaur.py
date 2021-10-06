class Dinosaur:
    def __init__(self, name, attack_power: int):
        self.name = name
        self.hp = 100
        self.attack_power = attack_power
    def attack_robot(self, robot: object):
        #TODO
        print(f"{self.name} attacking {robot.name}")
    def select_attack(attacks: tuple):
        #TODO
        print(f"Using {attack.name}")