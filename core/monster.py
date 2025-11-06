from abc import ABC, abstractmethod

class Monster(ABC):
    def __init__(self, name: str, hp: int, speed: int, power: int, armor_rating: int, weapon: str):
        self.name = name
        self.hp = hp
        self.speed = speed
        self.power = power
        self.armor_rating = armor_rating
        self.weapon = weapon

    @abstractmethod
    def attack(self):
        pass