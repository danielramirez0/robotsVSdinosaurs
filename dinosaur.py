class Dinosaur:
    def __init__(self, name, attack_power: int):
        self.name = name
        self.hp = 100
        self.attack_power = attack_power
        self.attacks = ("Slash", "Bite", "Stomp")
        self.attack = ''

    def attack_robot(self, robot):
        self.select_attack()
        robot.hp = robot.hp - int(self.attack_power)
        print(f"\n{self.name} attacked {robot.name} with {self.attack} for {self.attack_power} damage!\n{robot.name}'s HP is now {robot.hp}")
        if (robot.hp <= 0):
            print(f"\n{robot.name} has been destroyed!")

    def select_attack(self) -> str:
        print("\nSelect an attack: ")
        i = 1
        for attack in self.attacks:
            print(f"{i}: {attack}")
            i += 1
        self.attack = self.attacks[int(input("\nEnter # : ")) - 1]
