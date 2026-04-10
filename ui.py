class UI:
    def __init__(self):
        pass

    def render_score(self, score):
        print(f"Score: {score}")

    def render_game_state_message(self, message):
        print(message)

    def render_game_over_screen(self, final_score):
        print(f"Game Over! Final Score: {final_score}")
        print("Press 'R' to Restart")
