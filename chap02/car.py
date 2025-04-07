class car:
    def __init__(self, color, speed=0):
        # Constructor that gets called everytime the class is created
        self.color = color
        self.speed = speed

    def speed_up(self):
        self.speed += 10

    def speed_down(self):
        self.speed -= 10
