import sys
import pygame
from settings import Settings

def run_game():
    pygame.init()
    at_settings = Settings()
    screen = pygame.display.set_mode((at_settings.screen_width,at_settings.screen_height))
    pygame.display.set_caption("Invasion Alien")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        
        screen.fill(at_settings.bg_color)
        pygame.display.flip()

run_game()

