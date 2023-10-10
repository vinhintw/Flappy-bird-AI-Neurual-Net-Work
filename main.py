import pygame
from sys import exit
import config
import components
import population
import player

pygame.init()
clock = pygame.time.Clock()
population = population.Population(400)
player = player.Player()

def generate_pipes():
    config.pipes.append(components.Pipes(config.win_width))

def display_text(message, x, y, size, color):
        font = pygame.font.SysFont('Comic Sans Ms', size)
        text = font.render(message, True, color)
        config.window.blit(text, (x,y))

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
            pipes_spawn_time = 140
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

        # Display decision value
        #player.display_decision(config.window)
        display_text("Score: " + str(config.score),10, 10, 20, config.WHITE)
        display_text("Best score: " + str(config.best_score),10, 30, 20, config.WHITE)
        display_text("Best score of generation: " + str(config.best_score_of_generation),10, 50, 20, config.WHITE)

        clock.tick(60)
        pygame.display.flip()

main()
