import fleet
import herd
import robot
import dinosaur
import weapon


class Battlefield:
    def __init__(self):
        self.fleet = fleet.Fleet()
        self.herd = herd.Herd()

    def run_game(self):
        gatling_gun = weapon.Weapon("Gatling Gun", 70)
        laser_rifle = weapon.Weapon("Laser Rifle", 50)
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

        gaming = True

        while(gaming == True):
            self.battle(weapons)
            if (len(self.herd.dinosaurs) == 0):
                self.display_winners('Robots')
                gaming = False
            elif (len(self.fleet.robots) == 0):
                self.display_winners('Dinosaurs')
                gaming = False

    def display_welcome(self):
        print("\n\n\nWelcome to Robots VS Dinosaurs!\nRobots and Dinosaurs take turns attacking each other\nVictory happens when one team is destoyed!\n\n\n")
        print("ROBOTS!")
        for robot in self.fleet.robots:
            print(f"{robot.name}")
        print("\nDINOSAURS!")
        for dino in self.herd.dinosaurs:
            print(f"{dino.name}")

    def battle(self, weapons):
        for dino in self.herd.dinosaurs:
            self.dino_turn(dino)
        for robo in self.fleet.robots:
            self.robot_turn(robo, weapons)

    def dino_turn(self, dinosaur):
        if len(self.fleet.robots) > 0:
            print(f"\nIt's the {dinosaur.name}'s turn")
            self.show_robo_opponent_options()
            target = int(input('\nChoose target # : ')) - 1
            robo = self.fleet.robots[target]
            dinosaur.attack_robot(robo)
            if robo.hp <= 0:
                self.fleet.robots.remove(robo)

    def robot_turn(self, robot, weapons):
        if len(self.herd.dinosaurs) > 0:
            print(f"\nIt's {robot.name}'s turn")
            action = int(input("Select an action:\n1: Change weapon\n2: Attack\nEnter #: "))
            if action == 1:
                robot.select_weapon(weapons)
            self.show_dino_opponent_options()
            target = int(input('\nChoose target # : ')) - 1
            dino = self.herd.dinosaurs[target]
            robot.attack_dinosaur(dino)
            if dino.hp <= 0:
                self.herd.dinosaurs.remove(dino)

    def show_dino_opponent_options(self):
        print("\nThese are the available opponents to attack:")
        i = 1
        for dino in self.herd.dinosaurs:
            print(f"{i}: {dino.name}")
            i += 1

    def show_robo_opponent_options(self):
        print("\nThese are the available opponents to attack:")
        i = 1
        for robot in self.fleet.robots:
            print(f"{i}: {robot.name}")
            i += 1

    def display_winners(self, winner):
        if winner == "Dinosaurs":
            print("Dino VICTORY!")
        else:
            print("Robo VICTORY!")
