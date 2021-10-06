class Fleet:
    def __init__(self):
        self.robots = []
    def create_fleet(self, robots):
        for robot in robots:
            self.robots.append(robot)