# WRITE YOUR SOLUTION HERE:
# WRITE YOUR SOLUTION HERE:
import pygame
import random

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("src\\robot.png")

width = robot.get_width()
height = robot.get_height()

window.fill((0, 0, 0))

for i in range(1000):
    x = random.randint(1,640-width)
    y = random.randint(1, 480-height)
    window.blit(robot, (x, y))


pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()