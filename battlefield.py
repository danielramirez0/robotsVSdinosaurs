import fleet
import herd
import robot
import dinosaur
import weapon
import os

class Battlefield:
    def __init__(self):
        self.fleet = fleet.Fleet()
        self.herd = herd.Herd()
        self.clear = lambda: os.system('clear')
        self.players = 1
        self.useAI = True

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
        self.clear()
        print("\n\n**************************************************************************************")
        print("\t\tRobots VS Dinosaurs!\n\n\t\tRobots and Dinosaurs take turns attacking each other\n\n\t\tVictory happens when one team is destoyed!")
        print("**************************************************************************************\n\n")
        print("ROBOTS")
        print("------")
        for robot in self.fleet.robots:
            print(f"{robot.name}")
        print("\nDINOSAURS")
        print("---------")
        for dino in self.herd.dinosaurs:
            print(f"{dino.name}")
        self.players = int(input("\nSelect game type players:\n1: Sinlge Player\n2: Two Players\n\n#: "))

    def battle(self, weapons):
        for dino in self.herd.dinosaurs:
            self.dino_turn(dino)
        for robo in self.fleet.robots:
            self.robot_turn(robo, weapons)

    def dino_turn(self, dinosaur):
        self.clear()
        if len(self.fleet.robots) > 0:
            print(f"\nIt's the {dinosaur.name}'s turn")
            self.show_robo_opponent_options()
            target = int(input('\nChoose target # : ')) - 1
            robo = self.fleet.robots[target]
            dinosaur.attack_robot(robo)
            if robo.hp <= 0:
                self.fleet.robots.remove(robo)
            input("Continue...")

    def robot_turn(self, robot, weapons):
        self.clear()
        if len(self.herd.dinosaurs) > 0:
            print(f"\nIt's {robot.name}'s turn")
            action = int(input("\nSelect an action:\n1: Change weapon\n2: Attack\nEnter #: "))
            if action == 1:
                robot.select_weapon(weapons)
            self.show_dino_opponent_options()
            target = int(input('\nChoose target # : ')) - 1
            dino = self.herd.dinosaurs[target]
            robot.attack_dinosaur(dino)
            if dino.hp <= 0:
                self.herd.dinosaurs.remove(dino)
            input("Continue...")

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

    def prompt_input(question, valid):
        isValid = False
        response = ""
        while(not isValid or response == ""):
            response = input(question)
            isValid = valid(response)
        return response
    
    def autoValid(input):
        return True

    def is_within_length_of(array_length):
        return True