import math
import pygame
import random
def calculate_distance(enemy,player):
    return math.sqrt((enemy[0] - player[0])**2 + (enemy[1] - player[1])**2)

def calculate_vector(end_pos, start_pos, speed):
    dx, dy = end_pos[0] - start_pos[0], end_pos[1] - start_pos[1]
    distance = (dx**2 + dy**2) ** 0.5
    if distance == 0:
        return (0, 0)
    dx, dy = dx / distance * speed, dy / distance * speed
    return (dx, dy)

def draw_from_list(enemys,screen):
    for enemy in enemys:
        pygame.draw.rect(screen, enemy.color, enemy.rect)

def detect_collision(bullet,enemy):
    if bullet.rect.colliderect(enemy.rect):
        return True
    return False

def spawn_in_circle(center,game):
    n = random.randint(0,360)
    radius = random.randint(350,650)
    n = math.radians(n)

    pos_x = (math.cos(n) * radius) + center[0]
    pos_y = (math.sin(n) * radius) + center[1]
    
    return(pos_x,pos_y)
