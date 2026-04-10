# main_enhanced.py

import pygame
import random

# Constants for game state
MENU, PLAYING, PAUSED, GAME_OVER = 'menu', 'playing', 'paused', 'game_over'

# Constants for scoring based on asteroid size
ASTEROID_SCORES = {'large': 20, 'medium': 50, 'small': 100}

class GameManager:
    def __init__(self):
        self.score = 0
        self.lives = 3
        self.state = MENU

    def update_score(self, asteroid_size):
        if asteroid_size in ASTEROID_SCORES:
            self.score += ASTEROID_SCORES[asteroid_size]

    def decrement_life(self):
        self.lives -= 1
        if self.lives <= 0:
            self.state = GAME_OVER

    def reset_game(self):
        self.score = 0
        self.lives = 3
        self.state = MENU

def render_ui(screen, game_manager):
    font = pygame.font.Font(None, 36)
    score_text = font.render(f'Score: {game_manager.score}', True, (255, 255, 255))
    lives_text = font.render(f'Lives: {game_manager.lives}', True, (255, 255, 255))
    screen.blit(score_text, (10, 10))
    screen.blit(lives_text, (10, 50))

def display_menu(screen):
    font = pygame.font.Font(None, 60)
    title_text = font.render('Asteroids Game', True, (255, 255, 255))
    instructions_text = font.render('Press SPACE to start', True, (255, 255, 255))
    screen.blit(title_text, (screen.get_width()/2 - title_text.get_width()/2, screen.get_height()/2 - title_text.get_height()/2 - 20))
    screen.blit(instructions_text, (screen.get_width()/2 - instructions_text.get_width()/2, screen.get_height()/2 - instructions_text.get_height()/2 + 20))

def display_game_over(screen, game_manager):
    font = pygame.font.Font(None, 60)
    final_score_text = font.render(f'Final Score: {game_manager.score}', True, (255, 255, 255))
    restart_text = font.render('Press R to Restart or Q to Quit', True, (255, 255, 255))
    screen.blit(final_score_text, (screen.get_width()/2 - final_score_text.get_width()/2, screen.get_height()/2 - final_score_text.get_height()/2 - 20))
    screen.blit(restart_text, (screen.get_width()/2 - restart_text.get_width()/2, screen.get_height()/2 - restart_text.get_height()/2 + 20))

# Main game function (Placeholder)
if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    clock = pygame.time.Clock()
    game_manager = GameManager()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            # Handle menu, play, pause, and game over states.
        
        if game_manager.state == MENU:
            display_menu(screen)
        elif game_manager.state == GAME_OVER:
            display_game_over(screen, game_manager)
        else:
            render_ui(screen, game_manager)

        pygame.display.flip()
        clock.tick(60)