import pygame
import random

class Particle:
    def __init__(self, game, pos, size, speed, image):
        self.game = game
        self.pos = (pos[0] + random.randint(0, 15), pos[1] + random.randint(0, 15))
        self.size = size
        self.speed = speed + random.uniform(-0.05, 0.05)
        self.image = pygame.transform.scale(image, size)
        
        self.random_vector = (
            random.uniform(-self.speed, self.speed),
            random.uniform(-self.speed, self.speed)
        )

    def update(self):
        self.game.screen.blit(self.image, self.pos)
        self.pos = (self.pos[0] + self.random_vector[0], self.pos[1] + self.random_vector[1])