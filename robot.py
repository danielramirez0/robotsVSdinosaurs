import weapon
class Robot:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
        self.weapon = weapon()
    def attack(self, dinosaur):
        #TODO
        print(f"{self.name} attacked {dinosaur}")
    def select_weapon(self, weapons):
        #TODO
        print("Select weapon from list:")
        for weapon in weapons:
            print(f"{weapon.name}")
        self.weapon = weapon
        print(f"{weapon} attacked {dinosaur}")