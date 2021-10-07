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
        self.players = ['P1', 'P2']
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
            self.take_turns()
            if (len(self.herd.dinosaurs) == 0):
                self.display_winners('Robots')
                gaming = False
            elif (len(self.fleet.robots) == 0):
                self.display_winners('Dinosaurs')
                gaming = False

    def setup(self):
        gatling_gun = weapon.Weapon("Gatling Gun", 50, 50)
        laser_rifle = weapon.Weapon("Laser Rifle", 25, 25)
        pistol = weapon.Weapon("Pistol", 10, 10)
        fists = weapon.Weapon("Fists", 5, 5)
        self.weapons = [gatling_gun, laser_rifle, pistol, fists]

        t_1000 = robot.Robot("T-1000", self.weapons[3])
        t_800 = robot.Robot("T-800", self.weapons[3])
        t_101 = robot.Robot("T-101", self.weapons[3])

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

    def select_attacker(self, team):
        print("Select attacker:")
        i = 0
        for attacker in team:
            stat = "Energy" if hasattr(team[0], 'energy') else "Stamina"
            stat_value = attacker.energy if hasattr(team[0], 'energy') else attacker.stamina
            print(f"{i+1}: {attacker.name}, {stat}: {stat_value}, HP: {attacker.hp} ")
            i += 1
        chosen = self.prompt_input("# ", self.number_between, 1, len(team))
        return team[int(chosen) - 1]

    def take_turns(self):
        self.clear()
        for player in self.players:
            if player == "P2" and self.useAI == True:
                self.computer_turn()
            else:
                self.player_turn(player)

    def player_turn(self, player):
        self.clear()
        print(f"\nIt's {player}'s turn\n")
        team = self.fleet.robots if self.get_team(
            player) == "Robots" else self.herd.dinosaurs
        attacker = self.select_attacker(team)
        if self.get_team(player) == "Robots":
            self.robot_turn(attacker)
        else:
            self.dino_turn(attacker)

    def computer_turn(self):
        print("It's the computer's turn")

    def get_team(self, player):
        if player == "P1":
            return self.p1_team
        else:
            return self.p2_team

    def dino_turn(self, dinosaur):
        self.clear()
        if len(self.fleet.robots) > 0:
            print(f"\nSelect a target for the {dinosaur.name}:")
            self.show_robo_opponent_options()
            target = self.prompt_input(
                '\nChoose target # : ', self.number_between, 1, len(self.fleet.robots))
            robo = self.fleet.robots[int(target) - 1]
            dinosaur.attack_robot(robo)
            if robo.hp <= 0:
                self.fleet.robots.remove(robo)
            input("Continue...")

    def robot_turn(self, robot):
        self.clear()
        if len(self.herd.dinosaurs) > 0:
            print(f"\nSelect {robot.name}'s action")
            print(f"\nCurrently equipped weapon: {robot.weapon.name}")
            action = self.prompt_input(
                "\n1: Change weapon\n2: Attack\nEnter #: ", self.number_between, 1, 2)
            if int(action) == 1:
                robot.weapon.is_equipped = False
                robot.select_weapon(self.prompt_input,
                                    self.number_in, self.weapons)
            self.show_dino_opponent_options()
            target = self.prompt_input(
                '\nChoose target # : ', self.number_between, 1, len(self.herd.dinosaurs))
            dino = self.herd.dinosaurs[int(target) - 1]
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

    def number_in(self, input, arr):
        try:
            int(input)
        except:
            print('Only numbers are accepted')
            return False
        if int(input) in arr:
            return True
        else:
            print(f"Selection must be one of the following:")
            for number in arr:
                print(f"{number}")

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
