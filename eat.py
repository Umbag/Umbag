import pygame
import random

class eat():
    def __init__(self, eat_color, screen_width, screen_height):
        self.eat_color = eat_color
        self.eat_size_x = 10
        self.eat_size_y = 10
        self.eat_pos = [random.randrange(1, screen_width/10)*10,random.randrange(1, screen_height/10)*10]
    def draw_eat(self, play_surface):
        pygame.draw.rect(play_surface, self.eat_color, pygame.Rect(self.eat_pos[0], self.eat_pos[1],self.eat_size_x, self.eat_size_y))