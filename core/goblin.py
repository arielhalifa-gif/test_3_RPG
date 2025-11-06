# from monster import Monster
import game

class Goblin:
    def __init__(self, name: str, hp: int, speed: int, power: int, armor_rating: int, weapon: str):
        self.name = name
        self.hp = hp
        self.speed = speed
        self.power = power
        self.armor_rating = armor_rating
        self.weapon = weapon
        self.type = "goblin"

    def speak(self):
        print(f"the goblin {self.name} is angry")


    def attack(self):
        atacking_power = game.Game.roll_dice(6) + self.power
        weapons = ["knife", "sword", "garzen"]
        multiplying = [0.5, 1, 1.5]
        index = weapons.index(self.weapon)
        atacking_power *= multiplying[index]
        return atacking_power