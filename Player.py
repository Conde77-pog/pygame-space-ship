import pygame
import math
from Bullet import Bullet
from utils import calculate_distance, calculate_vector

class Player:
    def __init__(self, game, size, texture):
        self.game = game
        self.size = size
        self.pos = (self.game.screen.get_width() / 2, self.game.screen.get_height() / 2)
        self.rect = pygame.Rect(self.pos[0] - 16, self.pos[1] - 16, self.size[0], self.size[1])
        self.distances = []
        self.shoot_vector = (0, 0)
        self.close_enemy = None
        self.last_shot_time = 0
        self.shooting_delay = 25
        self.texture = texture
        self.heath = 200
        self.corrent_angle = 0
        self.rotated_texture = self.texture
    
    def update(self):
        if len(self.game.bullets) == 0:
            if self.last_shot_time >= self.shooting_delay:
                self.shoot_bullets(self.game.enemys)
                self.last_shot_time = 0
            self.last_shot_time += 1

        self.heath_rect = pygame.Rect(400, 10, self.heath, 25)
        self.full_heath_rect = pygame.Rect(400, 10, 200, 25)
        self.rotate_and_draw_texture(self.game.enemys)
        pygame.draw.rect(self.game.screen,(255,150,150),self.full_heath_rect)
        pygame.draw.rect(self.game.screen,(255,0,0),self.heath_rect)

        if self.heath <= 0:
            exit(0)

    def rotate_and_draw_texture(self, enemys):
        closest_enemy = self.get_closest_enemy(enemys)
        if closest_enemy:
            self.corrent_angle = self.calculate_angle(closest_enemy.pos)
            self.rotated_texture = pygame.transform.rotate(self.texture, self.corrent_angle)
            self.rect = self.rotated_texture.get_rect(center=self.rect.center)
        self.game.screen.blit(self.rotated_texture, self.rect)


    def get_closest_enemy(self, enemys):
        near_enemy = float('inf')
        closest_enemy = None
        
        for enemy in enemys:
            distance = calculate_distance(enemy.pos, self.pos)
            if distance <= self.game.shooting_area:
                if distance < near_enemy:
                    if self.close_enemy != enemy:
                        self.close_enemy = enemy
                    near_enemy = distance
                    closest_enemy = enemy

        return closest_enemy

    def calculate_angle(self, enemy_pos):
        delta_x = enemy_pos[0] - self.pos[0]
        delta_y = enemy_pos[1] - self.pos[1]
        angle = -math.degrees(math.atan2(delta_y, delta_x))
        return angle - 90
    
    def shoot_bullets(self, enemys):
        closest_enemy = self.get_closest_enemy(enemys)
        shoot_sound = pygame.mixer.Sound(r"sound\snare-space-shot-80932.mp3")
        if closest_enemy:
            shoot_sound.play()
            bullet_velocity = calculate_vector(closest_enemy.pos, self.pos, 5)
            self.game.bullets.append(Bullet((5, 5), self.pos, (255, 255, 255), self.game,pygame.image.load(r"sprites\Bullet.png").convert_alpha(), bullet_velocity))
