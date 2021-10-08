from random import randrange
class Dinosaur:
    def __init__(self, name, attack_power: int):
        self.name = name
        self.hp = 100
        self.stamina = 100
        self.attack_power = attack_power
        self.attacks = ("Slash", "Bite", "Stomp")
        self.attack = ''

    def attack_robot(self, robot):
        self.select_attack()
        robot.hp = robot.hp - int(self.attack_power)
        print(f"\n{self.name} attacked {robot.name} with {self.attack} for {self.attack_power} damage!\n{robot.name}'s HP is now {robot.hp}")
        if (robot.hp <= 0):
            print(f"\n{robot.name} has been destroyed!")
        self.stamina = self.stamina - 10

    def select_attack(self) -> str:
        i = randrange(len(self.attacks))
        self.attack = self.attacks[i]

    def __str__(self) -> str:
        return f"{self.name}  |  HP: {self.hp}  |  Stamina: {self.stamina}  |  Attack Power: {self.attack_power}"