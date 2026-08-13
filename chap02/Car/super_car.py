from typing import override

from .car import Car


class SuperCar(Car):
    def __init__(self, color: str, speed: int = 0, turbo: bool = True):
        super().__init__(color, speed)
        self.turbo: bool = turbo
        self.speed: int = speed

    def set_turbo(self, enabled: bool = True) -> None:
        self.turbo = enabled

    @override
    def speed_up(self) -> None:
        if self.turbo:
            self.speed += 50
        else:
            super().speed_up()
