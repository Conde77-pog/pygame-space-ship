import pygame
from utils import *

class Bullet:
    def __init__(self, size, pos,color,game,speed,velocity=(0, 0)):
        self.color = color
        self.game = game
        self.size = size
        self.pos = pos
        self.velocity = velocity
        self.rect = pygame.Rect(pos[0], pos[1], size[0], size[1])
        self.color = (255,255,255)
        self.damage = 0
        self.target = None
        self.speed = self.game.bullet_speed

    def update(self,end):
        self.target = end
        self.vector = calculate_vector(end.pos, self.pos, self.speed)
        self.pos = (self.pos[0] + self.vector[0], self.pos[1] + self.vector[1])
        self.rect.topleft = self.pos
        pygame.draw.rect(self.game.screen,self.color,self.rect)

        if self.target == None:
            self.game.bullets.remove(self)