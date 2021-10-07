
class Robot:
    def __init__(self, name, item):
        self.name = name
        self.hp = 100
        self.energy = 100
        self.weapon = item

    def attack_dinosaur(self, dinosaur):
        dinosaur.hp = dinosaur.hp - int(self.weapon.attack_power)
        print(f"\n{self.name} attacked {dinosaur.name} with {self.weapon.name} for {self.weapon.attack_power} damage!\n{dinosaur.name}'s HP is now {dinosaur.hp}")
        if (dinosaur.hp <= 0):
            print(f"\n{dinosaur.name} has been killed!")
        self.energy = self.energy - self.weapon.cost

    def select_weapon(self, prompt, callback, weapons: list):
        print("\nAvailable Weapons:")
        i = 1
        arr = []
        for weapon in weapons:
            if weapon.is_equipped == False:
                arr.append(i)
                print(f"{i}: {weapon.name}")
            i += 1
        selected_weapon = prompt("Select a weapon #: ", callback, arr)
        self.weapon = weapons[int(selected_weapon) - 1]
        self.weapon.is_equipped = True
        print(f"\n{self.weapon.name} selected")
