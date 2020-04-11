import pygame

class Snake():
    def __init__(self, window, headPos=[400, 400]):
        self.headPos = headPos
        self.window = window

    def moveSnake(self, control):
        if control.flagDirection == "DOWN":
            self.headPos[1] += 1
        elif control.flagDirection == "RIGHT":
            self.headPos[0] += 1
        elif control.flagDirection == "UP":
            self.headPos[1] -= 1
        elif control.flagDirection == "LEFT":
            self.headPos[0] -= 1

    def drawSnake(self):
        framesPerSecond = pygame.time.Clock()
        pygame.draw.rect(self.window, pygame.Color("white"), pygame.Rect(self.headPos[0], self.headPos[1], 30, 30))
        pygame.time.Clock().tick(60)
