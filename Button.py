import pygame
from Sheld import Sheld

class Button:
    def __init__(self, game, size, pos, color, tag,cost):
        self.font = pygame.font.Font(None, 20)
        self.game = game
        self.size = size
        self.pos = pos
        self.rect = pygame.Rect(self.pos[0], self.pos[1], self.size[0], self.size[1])
        self.color = color
        self.tag = tag 
        self.cost = cost
        self.text = tag
        self.upgrade_number = 1
        self.max = False
        self.mouse_pos = pygame.mouse.get_pos()
        self.hover_color = (min(color[0] + 50, 255), 
                            min(color[1] + 50, 255), 
                            min(color[2] + 50, 255))

    def update(self):
        self.mouse_pos = pygame.mouse.get_pos()
        self.draw_button()


    def draw_button(self):
        if self.rect.collidepoint(self.mouse_pos):
            pygame.draw.rect(self.game.screen, self.hover_color, self.rect)
        else:
            pygame.draw.rect(self.game.screen, self.color, self.rect)

        text_surface = self.font.render(f"{self.text} - {self.cost}", True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=self.rect.center)
        self.game.screen.blit(text_surface, text_rect)

    def check_input(self, event):
        if self.rect.collidepoint(self.mouse_pos):
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if self.tag == 'level':
                    if self.cost <= self.game.coins:
                        self.game.coins -= self.cost
                        self.game.level += 1
                        self.cost = int(self.cost * 1.5)
                    else:
                        print("You can't buy this upgrade: level")

                elif self.tag == 'bullet speed':
                    if self.max == False:
                        if self.cost <= self.game.coins:
                            self.game.coins -= self.cost
                            self.game.bullet_speed += 1
                            self.cost = int(self.cost * 1.5)
                            if self.game.bullet_speed == 25:
                                    self.text = 'MAX'
                                    self.color = (255,0,0)
                                    self.max = True
                    else:
                        print("You can't buy this upgrade: bullet speed")

                elif self.tag == 'shooting delay':
                    if self.max == False:
                        if self.cost <= self.game.coins:
                            self.game.coins -= self.cost
                            self.game.player.shooting_delay -= 1
                            self.cost = int(self.cost * 1.5)
                            if self.game.player.shooting_delay == 0:
                                self.text = 'MAX'
                                self.color = (255,0,0)
                                self.max = True
                    else:
                        print("You can't buy this upgrade: shooting delay")

                elif self.tag == 'shooting area':
                    if self.max == False:
                        if self.cost <= self.game.coins:
                            self.game.coins -= self.cost
                            self.game.shooting_area += 5
                            self.cost = int(self.cost * 1.5)
                            self.upgrade_number += 1
                            if self.upgrade_number >= 25:
                                    self.text = 'MAX'
                                    self.color = (255,0,0)
                                    self.max = True
                elif self.tag == 'sheeld':
                    if self.max == False:
                        if self.cost <= self.game.coins:
                            self.game.coins -= self.cost
                            self.game.sheelds.append(Sheld(self.game,(10,10),1,None))
                            self.upgrade_number += 1
                            if self.upgrade_number >= 15:
                                    self.text = 'MAX'
                                    self.color = (255,0,0)
                                    self.max = True

                    else:
                        print("You can't buy this upgrade: shooting area")
                
