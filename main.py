import game

if __name__ == "__main__":
    game.Game.start()
    choose = int(input())
    if choose == 1:
        player_name = input(f"choose the name of your player\n")
        player1 = game.Game.create_player(player_name)
        print(f"hello {player_name}")
        monster_name = input(f"choose the monster name\n")
        monster1 = game.Game.choose_random_monster(monster_name)
        print(f"hello {monster_name}")
        winner = game.Game.battle(player1, monster1)
        print(f"the winner is {winner.name}")
    print("good bye")