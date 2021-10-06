class Dinosaur:
    def __init__(self, name, attack_power: int):
        self.name = name
        self.hp = 100
        self.attack_power = attack_power
        self.attacks = ("Slash", "Bite", "Stomp")
    def attack_robot(self, robot):
        #TODO
        print(f"{self.name} attacking {robot}")
    def select_attack(self):
        print("Select an attack: ")
        i = 0
        for attack in self.attacks:
            print(f"{i + 1}: {attack}")