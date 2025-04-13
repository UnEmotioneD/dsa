class Car:
    def __init__(self, color: str, speed: int = 0):
        self.color = color
        self.speed = speed

    def speed_up(self) -> None:
        self.speed += 10

    def speed_down(self) -> None:
        self.speed -= 10

    def __str__(self) -> str:
        return f'{self.__class__.__name__}(Color: {self.color}, Speed: {self.speed})'
