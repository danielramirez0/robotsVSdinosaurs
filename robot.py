import weapon
class Robot:
    def __init__(self, name ):
        self.name = name
        self.hp = 100
        self.weapon = weapon()
    def attack(self, dinosaur: object):
        #TODO
        print(f"{self.name} attacked {dinosaur.name}")
    def select_weapon(self, weapons: list):
        #TODO
        print("Select weapon from list:")
        for weapon in weapons:
            print(f"{weapon.name}")
        self.weapon = weapon
        print(f"{weapon} selected")