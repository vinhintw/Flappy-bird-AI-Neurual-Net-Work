import pygame
from sys import exit
import config
import components
import population
import player

pygame.init()
clock = pygame.time.Clock()
population = population.Population(100)
player = player.Player()



def main():
    pipes_spawn_time = 10
    while True:
        config.quit_game()
        config.window.fill(config.BLACK)

        #Spawn Ground
        config.ground.draw(config.window)

        #Spawn Pipes:
        if pipes_spawn_time <= 0:
            config.generate_pipes()
            pipes_spawn_time = 135
        pipes_spawn_time -= 1

        for p in config.pipes:
            p.draw(config.window)
            p.update()
            if p.off_screen:
                config.pipes.remove(p)
                config.score += 1

        if not population.extinct():
            population.update_live_players()
        else:
            config.pipes.clear()    #CLear pipes before create new generation player
            population.natural_selection()
            config.score = 0

        config.draw_text()

        clock.tick(60)
        pygame.display.flip()

main()
