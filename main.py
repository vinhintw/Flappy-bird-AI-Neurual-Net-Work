import pygame
from sys import exit
import config

pygame.init
clock = pygame.time.Clock()

def quit_game():
    for envent in pygame.event.get():
        if envent.type == pygame.QUIT:
            pygame.quit()
            exit()

def main():
    while True:
        quit_game()
        config.window.fill(config.BLACK)

        #Spawn Ground
        config.ground.draw(config.window)

        clock.tick(60)
        pygame.display.flip()

main()
