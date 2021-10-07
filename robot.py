import weapon


class Robot:
    def __init__(self, name):
        self.name = name
        self.hp = 100
        self.weapon = weapon.Weapon("Fists", 5)

    def attack_dinosaur(self, dinosaur):
        dinosaur.hp = dinosaur.hp - int(self.weapon.attack_power)
        print(f"\n{self.name} attacked {dinosaur.name} with {self.weapon.name} for {self.weapon.attack_power} damage!\n{dinosaur.name}'s HP is now {dinosaur.hp}")
        if (dinosaur.hp <= 0):
            print(f"\n{dinosaur.name} has been killed!")

    def select_weapon(self, weapons: list):
        i = 1
        print("\nAvailable Weapons:")
        for weapon in weapons:
            if weapon.is_equipped == False:
                print(f"{i}: {weapon.name}")
            i += 1
        selected_weapon = int(input("Select a weapon #: ")) - 1
        self.weapon = weapons[selected_weapon]
        self.weapon.is_equipped = True
        print(f"\n{self.weapon.name} selected")
