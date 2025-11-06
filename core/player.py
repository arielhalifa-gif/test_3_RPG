import game

class Player:
    def __init__(self, name:str, hp: int, speed: int, power: int, armor_rating: int, profession: str):
        self.name = name
        self.hp = hp
        self.speed = speed
        self.power = power
        self.armor_rating = armor_rating
        self.profession = profession


    def speak(self):
        print(f"the player {self.name} doing great")

    def attack(self):
        atacking_power = game.Game.roll_dice(6) + self.power
        return atacking_power