
from random import choice


class Robot:
    def __init__(self, name, item):
        self.name = name
        self.hp = 100
        self.energy = 100
        self.weapon = item

    def attack_dinosaur(self, dinosaur):
        dinosaur.hp = dinosaur.hp - int(self.weapon.attack_power)
        print(f"\n{self.name} attacked {dinosaur.name} with {self.weapon.name} for {self.weapon.attack_power} damage!\n\n{dinosaur.name}'s HP is now {dinosaur.hp}")
        if (dinosaur.hp <= 0):
            print(f"\n{dinosaur.name} has been killed!")
        self.energy = self.energy - self.weapon.cost

    def select_weapon(self, prompt, callback, weapons: list, use_ai=False):
        print("\nAvailable Weapons:")
        i = 1
        arr = []
        for weapon in weapons:
            if weapon.is_equipped == False:
                arr.append(i)
                print(
                    f"{i}: {weapon.name}\t|\tPower: {weapon.attack_power}\t|\tEnergy Cost: {weapon.cost}")
            i += 1
        if use_ai == False:
            selected_weapon = prompt("\n#: ", callback, arr)
            self.weapon = weapons[int(selected_weapon) - 1]
        else:
            random_weapon = choice(weapons)
            self.weapon = random_weapon
        self.weapon.is_equipped = True
        print(f"\n{self.weapon.name} selected")

    def __str__(self) -> str:
        return f"{self.name}  |  HP: {self.hp}  |  Energy: {self.energy}  |  Weeapon: {self.weapon.name}  |  Energy Drain: {self.weapon.cost}  |  Power: {self.weapon.attack_power}"
