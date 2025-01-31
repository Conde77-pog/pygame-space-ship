import pygame
import sys
import random
import os
from utils import *
from Enemy import Enemy
from Player import Player
from Button import Button
from Particle import Particle

class Game:
    def __init__(self):
        pygame.init()
        self.coins = 0
        self.screen = pygame.display.set_mode((640, 800))
        self.bullet_speed = 5
        self.running = True
        self.clock = pygame.time.Clock()
        self.enemys = []
        self.bullets = []
        self.sheelds = []
        self.particles = []
        self.level = 1
        self.player = Player(self,(32,32),texture=pygame.image.load(r"sprites\main_shipe.png").convert_alpha())
        self.screen_center = (self.screen.get_width() / 2,self.screen.get_height() / 2)
        self.shooting_area = 150
        self.font = pygame.font.Font(None,36)

    def run(self):
        self.button()
        while self.running:
            if len(self.enemys) <= 1:
                self.add_enemys()
            #fill the screen
            self.screen.fill((0,0,0))
            pygame.draw.circle(self.screen,(200,200,200),self.screen_center,self.shooting_area,2)
            #update the player
            self.player.update()
            #draw the enemy
            draw_from_list(self.enemys,self.screen)
            #draw the bullets
            draw_from_list(self.bullets,self.screen)


            self.clock.tick(60)
            self.handle_events()
            self.update()
            pygame.display.flip()
        
        pygame.quit()
        sys.exit()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            
            for button in self.upgrade_buttons:
                button.check_input(event)

    def update(self):

        coins_textured = self.font.render(f"COINS -> {self.coins}",True,(255,255,255))
        self.screen.blit(coins_textured , (0, 0))

        # Loop through the enemies and update
        enemies_to_remove = []
        for enemy in self.enemys:
            if calculate_distance(self.screen_center, enemy.pos) <= 25:
                crash_sound = pygame.mixer.Sound(r"sound\launch-85216.mp3")
                crash_sound.play()
                self.player.heath -= 20
                enemies_to_remove.append(enemy)
            else:
                enemy.update(self.screen)

        # Remove enemies after loop (to avoid modifying the list while iterating)
        for enemy in enemies_to_remove:
            self.enemys.remove(enemy)

        # Loop through the bullets and update
        bullets_to_remove = []
        for bullet in self.bullets[:]:
            bullet.update(self.player.close_enemy)
            if bullet.target is None:
                self.bullets.remove(bullet)
            else:
                for enemy in self.enemys[:]:
                    if detect_collision(bullet, enemy):
                        explode_sound = pygame.mixer.Sound(r"sound\explosion-sound-effect-1-free-on-gamesfxpackscom-241821.mp3")
                        explode_sound.play()
                        self.coins += random.randint(1, 3) * self.level
                        for _ in range(7):
                            rand_size = random.randint(16,32)
                            self.particles.append(Particle(self, list(enemy.pos), (rand_size, rand_size), 1, pygame.image.load(r"sprites\rock_particle.png").convert_alpha()))
                        self.bullets.remove(bullet)
                        if enemy in self.enemys:
                            self.enemys.remove(enemy)
                        break

        # Remove bullets after checking collisions (to avoid modifying the list while iterating)
        for bullet in bullets_to_remove:
            self.bullets.remove(bullet)

        #update buttons 
        for button in self.upgrade_buttons:
            button.update()
        
        for particle in self.particles[:]:  # Use a copy of the list for safe iteration
            particle.update()
            if (particle.pos[1] > self.screen.get_height() or particle.pos[1] < 0 or
                particle.pos[0] > self.screen.get_width() or particle.pos[0] < 0):
                self.particles.remove(particle)
        #update sheeld
        for sheeld in self.sheelds:
            sheeld.update()
            for enemy in self.enemys:
                if sheeld.rect.colliderect(enemy.rect):
                    explode_sound = pygame.mixer.Sound(r"sound\explosion-sound-effect-1-free-on-gamesfxpackscom-241821.mp3")
                    explode_sound.play()
                    for _ in range(7):
                        rand_size = random.randint(16,32)
                        self.particles.append(Particle(self, list(enemy.pos), (rand_size, rand_size), 1, pygame.image.load(r"sprites\rock_particle.png").convert_alpha()))
                    self.coins += random.randint(1,3) * self.level
                    if enemy in self.enemys:
                        self.enemys.remove(enemy)


    def add_enemys(self):
        number_of_enemys = random.randint(1, self.level)
        for i in range(0, number_of_enemys):
            rand = random.randint(1, self.level)
            pos = spawn_in_circle(self.screen_center,self)
            self.enemys.append(Enemy((32,32),pos,rand,pygame.image.load(r"sprites\asteroid.png").convert_alpha()))

    def button(self):
        self.upgrade_buttons = []

        self.upgrade_buttons.append(Button(self,(150,30),(0,self.screen.get_height()- 50),(0,0,255),'level',20))
        self.upgrade_buttons.append(Button(self,(150,30),(160,self.screen.get_height()- 50),(0,0,255),'bullet speed',10))
        self.upgrade_buttons.append(Button(self,(150,30),(320,self.screen.get_height()- 50),(0,0,255),'shooting delay',15))
        self.upgrade_buttons.append(Button(self,(150,30),(480,self.screen.get_height()- 50),(0,0,255),'shooting area',10))
        self.upgrade_buttons.append(Button(self,(150,30),(480,self.screen.get_height()- 100),(0,0,255),'sheeld',50))

game = Game()
game.run()