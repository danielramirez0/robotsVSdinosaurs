class Robot:
    def __init__(self, name ):
        self.name = name
        self.hp = 100
        self.weapon = 'None'
    def attack(self, dinosaur):
        #TODO
        print(f"{self.name} attacked {dinosaur}")
    def select_weapon(self, weapons: list):
        i = 0
        print("Weapons")
        for weapon in weapons:
            print(f"{i + 1}: {weapon.name}")
            i += 1
        selected_weapon = input("Select a weapon #: ")
        self.weapon = selected_weapon
        print(f"{weapon} selected")