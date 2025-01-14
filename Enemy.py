import pygame
from utils import calculate_vector

class Enemy:
    def __init__(self, size, pos,speed,velocity=(0, 0)):
        self.size = size
        self.pos = pos
        self.velocity = velocity
        self.rect = pygame.Rect(pos[0], pos[1], size[0], size[1])
        self.color = (200, 100, 200)
        self.heath = 0
        self.speed = speed

    def update(self, screen):
        end_pos = (screen.get_width() / 2,screen.get_height()/ 2)
        self.vector = calculate_vector(end_pos,self.pos,self.speed)
        self.pos = (self.pos[0] + self.vector[0], self.pos[1] + self.vector[1])
        self.rect.topleft = self.pos
        