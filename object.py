import pygame

class Object():
    def __init__(self):
        self.size = 20
        self.color = "red"
        self.position = [780, 580]

    def drawObject(self):
        pygame.draw.rect(self.window, self.color, pygame.Rect(random.randrange(self.position[0], self.position[1], self.size, self.size)),random.randrange(self.position[0], self.position[1], self.size, self.size)
