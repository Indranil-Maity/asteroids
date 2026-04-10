class Game:
    def __init__(self):
        self.state = 'MENU'

    def change_state(self, new_state):
        if new_state in ['MENU', 'PLAYING', 'GAME_OVER', 'PAUSED']:
            self.state = new_state
            print(f"Game state changed to: {self.state}")
        else:
            print(f"Invalid state: {new_state}")

    def update(self):
        if self.state == 'PLAYING':
            self.play()
        elif self.state == 'GAME_OVER':
            self.game_over()
        elif self.state == 'PAUSED':
            self.pause()

    def play(self):
        print("Gameplay started.")
        # Implement game logic here

    def game_over(self):
        print("Game Over. You lost the game.")
        # Handle game over logic here

    def pause(self):
        print("Game paused.")
        # Implement pause logic here

if __name__ == '__main__':
    game = Game()
    game.change_state('PLAYING')
    game.update()
    game.change_state('PAUSED')
    game.update()
    game.change_state('GAME_OVER')
    game.update()