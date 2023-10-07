import pygame
from sys import exit
import config
import components

pygame.init
clock = pygame.time.Clock()

def generate_pipes():
    config.pipes.append(components.Pipes(config.win_width))


def quit_game():
    for envent in pygame.event.get():
        if envent.type == pygame.QUIT:
            pygame.quit()
            exit()

def main():
    pipes_spawn_time = 10
    while True:
        quit_game()
        config.window.fill(config.BLACK)

        #Spawn Ground
        config.ground.draw(config.window)

        #Spawn Pipes:
        if pipes_spawn_time <= 0:
            generate_pipes()
            pipes_spawn_time = 200
        pipes_spawn_time -= 1

        for p in config.pipes:
            p.draw(config.window)
            p.update()
            if p.off_screen:
                config.pipes.remove(p)


        clock.tick(60)
        pygame.display.flip()

main()
