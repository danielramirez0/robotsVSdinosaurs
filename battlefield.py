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
        self.useAI = bool
        self.p1_team = str
        self.p2_team = str
        self.weapons = []

    def run_game(self):

        self.setup()

        self.display_welcome()

        self.select_game_type()

        self.select_teams()

        gaming = True
        while(gaming == True):
            self.battle()
            if (len(self.herd.dinosaurs) == 0):
                self.display_winners('Robots')
                gaming = False
            elif (len(self.fleet.robots) == 0):
                self.display_winners('Dinosaurs')
                gaming = False

    def setup(self):
        gatling_gun = weapon.Weapon("Gatling Gun", 70)
        laser_rifle = weapon.Weapon("Laser Rifle", 50)
        pistol = weapon.Weapon("Pistol", 10)
        self.weapons = [gatling_gun, laser_rifle, pistol]

        t_1000 = robot.Robot("T-1000")
        t_800 = robot.Robot("T-800")
        t_101 = robot.Robot("T-101")

        t_rex = dinosaur.Dinosaur("T-Rex", 50)
        raptor = dinosaur.Dinosaur("Raptor", 30)
        triceratops = dinosaur.Dinosaur("Triceratops", 20)

        self.fleet.create_fleet([t_1000, t_800, t_101])
        self.herd.create_herd([t_rex, raptor, triceratops])

    def select_game_type(self):
        game_type_messsage = "\nSelect game type:\n1: Single Player\n2: Two Players\n\n#: "
        game_type = int(self.prompt_input(
            game_type_messsage, self.number_between, 1, 2))
        self.useAI = True if game_type == 1 else False

    def select_teams(self):
        self.p1_selection = self.prompt_input(
            "\nSelect your team:\n1: Robots\n2: Dinosaurs\n\n#: ", self.number_between, 1, 2)
        if self.p1_selection == "1":
            self.p1_team = 'Robots'
            self.p2_team = 'Dinosaurs'
        else:
            self.p1_team = 'Dinosaurs'
            self.p2_team = 'Robots'

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

    def battle(self):
        for dino in self.herd.dinosaurs:
            self.dino_turn(dino)
        for robo in self.fleet.robots:
            self.robot_turn(robo)

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

    def robot_turn(self, robot):
        self.clear()
        if len(self.herd.dinosaurs) > 0:
            print(f"\nIt's {robot.name}'s turn")
            action = int(
                input("\nSelect an action:\n1: Change weapon\n2: Attack\nEnter #: "))
            if action == 1:
                robot.select_weapon(self.weapons)
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

    def prompt_input(self, question, valid, opt_param_1=False, opt_param_2=False):
        isValid = False
        response = ""
        while(not isValid or response == ""):
            response = input(question)
            if opt_param_1 and opt_param_2:
                isValid = valid(response, opt_param_1, opt_param_2)
            elif opt_param_1:
                isValid = valid(response, opt_param_1)
            else:
                isValid = valid(response)
        return response

    def auto_valid(self, input):
        return True

    def number_between(self, input, a, b):
        try:
            int(input)
        except:
            print('Only numbers are accepted')
            return False
        if int(input) >= a and int(input) <= b:
            return True
        else:
            print(f"Selection must be between {a} and {b}")

    def is_within_length_of(self, array_length):
        return True
