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

window = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("Flappy bird A.I Neural Network Algorithm")


ground = components.Ground(win_width)
pipes = []
