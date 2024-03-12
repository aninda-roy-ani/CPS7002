# Presentation Layer

class GameInterface:

    def play_game(self, game):
        print("Welcome to the Dungeon!")
        while game.player_health > 0:
            print("\nCurrent Room:", self.current_room)
            action = input("Enter your action (move/fight): ").lower().strip()
            if action == "move":
                game.move()
            elif action == "fight":
                game.fight()
            else:
                print("Invalid action! Please try again.")



