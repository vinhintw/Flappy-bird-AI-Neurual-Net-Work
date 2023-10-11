import pygame
import components
import player

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
win_height = 720
win_width = 550
score = 0  # Best Score
best_score = 0
best_score_of_generation = 0



def generate_pipes():
    pipes.append(components.Pipes(win_width))

def quit_game():
    for envent in pygame.event.get():
        if envent.type == pygame.QUIT:
            pygame.quit()
            exit()

def display_text(message, x, y, size, color):
        font = pygame.font.SysFont('Comic Sans Ms', size)
        text = font.render(message, True, color)
        window.blit(text, (x,y))

def draw_text():
        display_text("Score: " + str(score),10, 10, 20, WHITE)
        display_text("Best score: " + str(best_score),10, 30, 20, WHITE)
        display_text("Best score of generation: " + str(best_score_of_generation),10, 50, 20, WHITE)


window = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("Flappy bird A.I Neural Network Algorithm")




ground = components.Ground(win_width)
pipes = []
