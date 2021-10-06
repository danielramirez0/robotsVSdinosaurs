class Herd:
    def __init__(self):
        self.dinosaurs = []
    def create_herd(self, dinosaurs):
        for dinosaur in dinosaurs:
            self.dinosaurs.append(dinosaur)