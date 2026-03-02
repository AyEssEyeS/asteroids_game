import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state
from player import Player

import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state

def main():
    my_player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    
    while (True):
        log_state()
        for event  in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        my_player.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000
        

    

if __name__ == "__main__":
    main()
