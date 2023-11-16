import random

from car import Car

STARTING_MOVE_DISTANCE = 100
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.list = []
        for n in range(0, 4):
            for i in range(0, 4):
                car = Car((
                    (i * 150 + random.random() * 75) * (-1 ** random.randint(1, 2)),
                    (n + 1) * 80 - 150), MOVE_INCREMENT)
                self.list.append(car)

    def move(self):
        for n in self.list:
            n.forward(MOVE_INCREMENT)

    def collide(self, player):
        for n in self.list:
            if n.collide(player):
                return True
        return False
