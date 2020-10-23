import sys
import pygame
import game_functions as gf
from settings import Settings
from ship import Ship


def run_game():
    # Initialize game and create a screen object.
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Alien Invasion")
    
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    
    # Make a ship.
    ship = Ship(screen)

    # Start the main loop for the game.
    while True:
        gf.check_events()
        gf.update_screen(ai_settings, screen, ship)

        # Make the most recently drawn screen visible.
        pygame.display.flip()
run_game()