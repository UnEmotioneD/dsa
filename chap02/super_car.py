from car import car  # car class from car.py (module)


class super_car(car):
    # super_car is child class of car class
    def __init__(self, color, speed=0, b_turbo=True):
        # constructor
        super().__init__(color, speed)
        self.b_turbo = b_turbo

    def set_turbo(self, b_turbo=True):
        self.b_turbo = b_turbo

    def speed_up(self):
        if self.b_turbo:
            self.speed += 50
        else:
            super().speed_up()
