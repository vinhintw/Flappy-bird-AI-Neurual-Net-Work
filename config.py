import pygame
import components


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
win_height = 720
win_width = 550
score = 0



window = pygame.display.set_mode((win_width, win_height))

ground = components.Ground(win_width)
pipes = []
