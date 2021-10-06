import fleet, herd, robot, dinosaur, weapon
class Battlefield:
    def __init__(self):
        self.fleet = fleet.Fleet()
        self.herd = herd.Herd()
    def run_game(self):
        gatling_gun = weapon.Weapon("Gatling Gun", 60)
        laser_rifle = weapon.Weapon("Laser Rifle", 25)
        pistol = weapon.Weapon("Pistol", 10)
        weapons = [gatling_gun, laser_rifle, pistol]

        t_1000 = robot.Robot("T-1000")
        t_800 = robot.Robot("T-800")
        t_101 = robot.Robot("T-101")

        t_rex = dinosaur.Dinosaur("T-Rex", 50)
        raptor = dinosaur.Dinosaur("Raptor", 30)
        triceratops = dinosaur.Dinosaur("Triceratops", 20)

        self.fleet.create_fleet([t_1000, t_800, t_101])
        self.herd.create_herd([t_rex, raptor, triceratops])

        self.display_welcome()
        #TODO
    def display_welcome(self):
        print("Welcome to Robots VS Dinosaurs!\nRobots and Dinosaurs take turns attacking each other\nVictory happens when one team is destoyed!\n\nHere are the robots:")
        for robot in self.fleet.robots:
            print(f"{robot.name}")
        print("\n\nHere are the Dinosaurs:")
        for dino in self.herd.dinosaurs:
            print(f"{dino.name}")
    def battle(self):
        #TODO
        return
    def dino_turn(self, dinosaur):
        #TODO
        return
    def robot_turn(self, robot):
        #TODO
        return
    def show_dino_opponent_options(self):
        #TODO
        return
    def show_robo_opponent_options(self):
        #TODO
        return
    def display_winners(self):
        #TODO
        return