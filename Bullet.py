import pygame
from utils import *

class Bullet:
    def __init__(self, size, pos,color,game,texture,velocity=(0, 0)):
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
        self.texture = texture
        self.angle_texture = texture

    def update(self,end):
        self.target = end
        self.vector = calculate_vector(end.pos, self.pos, self.speed)
        self.pos = (self.pos[0] + self.vector[0], self.pos[1] + self.vector[1])
        self.rect.topleft = self.pos
        self.angle_texture = pygame.transform.rotate(self.texture,self.calculate_angle(self.game.player.get_closest_enemy(self.game.enemys)))

        if self.target == None:
            self.game.bullets.remove(self)

        
    def calculate_angle(self, enemy):
        if enemy is None:
            return 0  # Default angle or handle the case appropriately
        
        delta_x = enemy.pos[0] - self.pos[0]
        delta_y = enemy.pos[1] - self.pos[1]
        angle = -math.degrees(math.atan2(delta_y, delta_x))
        return angle - 90