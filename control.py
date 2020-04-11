import pygame
import sys

class Controls():
    def __init__(self, flagDirection = "RIGHT"):
        self.flagDirection = flagDirection

    def control(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if self.flagDirection != "DOWN" and event.key == pygame.K_DOWN:
                    self.flagDirection = "DOWN"
                    
                elif self.flagDirection != "RIGHT" and event.key == pygame.K_RIGHT:
                    self.flagDirection = "RIGHT"
                    
                elif self.flagDirection != "UP" and event.key == pygame.K_UP:
                    self.flagDirection = "UP"
                    
                elif self.flagDirection != "LEFT" and event.key == pygame.K_LEFT:
                    self.flagDirection = "LEFT"