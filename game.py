import random
from core.player import Player
from core.goblin import Goblin
from core.orc import Orc

class Game:
    @staticmethod
    def start():
        print(f"welcome to the game please choose your game")
        Game.show_menu()


    @staticmethod
    def show_menu():
        print(f"star fight: -> 1\nexit: -> 0")

    @staticmethod
    def create_player(name):
        random_choose = random.randint(0,1)
        power = random.randint(5,10)
        speed = random.randint(5,10)
        armor_rating = random.randint(5,15)
        hp = 50
        if random_choose == 1:
            profession = "warrior"
            power += 2
        else:
            profession = "healing"
            hp += 10
        player = Player(name, hp, speed, power, armor_rating, profession)
        return player
    
    @staticmethod
    def choose_random_monster(name):
        random_choose = random.randint(0,1)
        weapon_index = random.randint(0,2)
        weapons = ["knife", "sword", "garzen"]
        if random_choose == 1: #orc
            speed = random.randint(0,5)
            power = random.randint(10,15)
            armor_rating = random.randint(2,8)
            monster = Orc(name, 50, speed, power, armor_rating, weapons[weapon_index])
        else: #goblin
            speed = random.randint(5,10)
            power = random.randint(5,10)
            monster = Goblin(name, 20, speed, power, 1, weapons[weapon_index])
        return monster


    @staticmethod
    def battle(player, monster):
        dice_player = Game.roll_dice(6) + player.speed
        dice_monster = Game.roll_dice(6) + monster.speed
        if dice_player >= dice_monster:
            atacking = player
            atacked = monster
        else:
            atacking = monster
            atacked = player
        stil_alive = True
        while stil_alive:
            calculate_atack = Game.roll_dice(20) + atacking.speed
            if calculate_atack > atacked.armor_rating: # פגיעה
                atacked.hp -= atacking.attack()
                atacked.speak()
                if atacked.hp < 0:
                    stil_alive = False
            atacking, atacked = atacked, atacking
        if atacking.name == player.name:
            return monster
        else:
            return player


            
    @staticmethod
    def roll_dice(sides):
        return random.randint(1,sides)