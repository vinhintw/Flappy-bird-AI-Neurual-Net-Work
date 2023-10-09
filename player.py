import pygame
import random
import config
import brain


class Player:
    def __init__(self):
        self.x, self.y = 50, 200
        self.rect = pygame.Rect(self.x, self.y, 20, 20)
        self.color = random.randint(100, 255), random.randint(100, 255), random.randint(100, 255)
        self.vel = 0
        self.flap = False
        self.alive = True

        # AI
        self.decision = None
        self.vision = [0.5, 1, 0.5]
        self.inputs = 3
        self.brain = brain.Brain(self.inputs)
        self.brain.generate_net()


    #Game ralated function
    def draw (self, window):
        pygame.draw.rect(window, self.color, self.rect)

    def ground_collision(self, ground):
        return pygame.Rect.colliderect(self.rect, ground)
    
    def sky_collision(self):
        return bool(self.rect.y < 30)
    
    def pipe_collision(self):
        for p in config.pipes:
            return pygame.Rect.colliderect(self.rect, p.top_rect) or \
                   pygame.Rect.colliderect(self.rect, p.bottom_rect)
        
    def update(self, ground):
        if not (self.ground_collision(ground) or self.pipe_collision() ):

            #Gravity
            self.vel += 0.25
            self.rect.y += self.vel
            if self.vel >5:
                self.vel = 5
        else:
            self.alive = False
            self.flap = False
            self.vel = 0

    def bird_flap(self):
        if not self.flap and not self.sky_collision():
            self.flap = True
            self.vel = -5
        if self.vel >=3:
            self.flap = False

    @staticmethod
    def closest_pipe():
        for p in config.pipes:
            if not p.passed:
                return p

    #AI related function
    def look(self):
        if config.pipes:
            # Calculate coordinates for lines
            top_pipe = self.closest_pipe().top_rect
            bottom_pipe = self.closest_pipe().bottom_rect
            top_pipe_x = top_pipe.centerx
            top_pipe_bottom = top_pipe.bottom
            bottom_pipe_x = bottom_pipe.centerx
            bottom_pipe_top = bottom_pipe.top

            # Line to top pipe
            self.vision[0] = max(0, self.rect.center[1] - top_pipe_bottom) / 500
            pygame.draw.line(config.window, self.color, self.rect.center,
                            (top_pipe_x, top_pipe_bottom))

            # Line to mid pipe (the x-coordinate is already calculated)
            self.vision[1] = max(0, bottom_pipe_x - self.rect.center[0]) / 500
            #pygame.draw.line(config.window, self.color, self.rect.center,
            #                (bottom_pipe_x, self.rect.center[1]))

            # Line to bottom pipe
            self.vision[2] = max(0, bottom_pipe_top - self.rect.center[1]) / 500
            pygame.draw.line(config.window, self.color, self.rect.center,
                            (bottom_pipe_x, bottom_pipe_top))


    def think(self):
        self.decision = self.brain.feed_forward(self.vision)
        if self.decision > 0.73:
            self.bird_flap()

        