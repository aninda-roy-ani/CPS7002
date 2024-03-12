from interface import GameInterface


class Game(GameInterface):
    def __init__(self):
        self.current_room = "Entrance"
        self.player_health = 100
        self.player_inventory = []

    def move(self):
        print("You move to another room.")
        # Code to handle movement logic
        pass

    def fight(self):
        print("You encounter a monster!")
        # Code to handle combat logic
        pass

# Instantiate and play the game
game = Game()
game.play_game(game)