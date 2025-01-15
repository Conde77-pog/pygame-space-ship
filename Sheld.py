import pygame
import math

class Sheld:
    def __init__(self, game, size, speed, texture):
        self.game = game
        self.size = size
        self.speed = speed
        self.pos = (self.game.screen.get_width() / 2, self.game.screen.get_height() / 2)
        self.rect = pygame.Rect(self.pos[0], self.pos[1], self.size[0], self.size[1])
        self.texture = texture
        self.angle = 0

    def update(self):
        self.get_pos()
        self.rect.topleft = (self.pos[0] - self.size[0] // 2, self.pos[1] - self.size[1] // 2)
        pygame.draw.rect(self.game.screen,(150,150,255),self.rect)

    def get_pos(self):
        self.angle += self.speed
        
        center_x = self.game.screen.get_width() / 2
        center_y = self.game.screen.get_height() / 2
        
        self.pos = (
            center_x + math.cos(math.radians(self.angle)) * (self.game.shooting_area + 32),
            center_y + math.sin(math.radians(self.angle)) * (self.game.shooting_area + 32)
        )
