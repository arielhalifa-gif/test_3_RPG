from monster import Monster
import game

class Goblin(Monster):
    def __init__(self, name, hp, speed, power, armor_rating, weapon):
        super().__init__(name, hp, speed, power, armor_rating, weapon)
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