import pygame
import random

import control
import snake
import object

pygame.init()
window = pygame.display.set_mode((800, 600))
ctrl = control.Controls()
snake = snake.Snake(window)
objs = object.Object()




if __name__ == "__main__":
    while True:
        ctrl.control()
        window.fill(pygame.Color(0, 255, 0))
        for obj in objs:
            obj.drawObject()
        snake.moveSnake(ctrl)
        snake.drawSnake()
        pygame.display.update()
