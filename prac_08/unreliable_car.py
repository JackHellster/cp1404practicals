from prac_08.car import Car
import random


class UnreliableCar(Car):
    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        self.distance_travelled = 0
        self.reliability = reliability


    def __str__(self):
        return f"{super().__str__()}, {self.distance_travelled}km driven, reliability: {self.reliability}%"

    def drive(self, distance):
        i = random.randint(1, 100)
        if self.reliability < i:
            drive_distance = super().drive(0)
            return drive_distance
        else:
            drive_distance = super().drive(distance)
            self.distance_travelled += drive_distance
            return drive_distance