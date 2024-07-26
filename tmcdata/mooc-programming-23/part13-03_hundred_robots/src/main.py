# WRITE YOUR SOLUTION HERE:
import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("src\\robot.png")

width = robot.get_width()
height = robot.get_height()

window.fill((0, 0, 0))

i = 0
j = 0

while i < 200:
    while j < 100:
        window.blit(robot, (j + 40, i))
        window.blit(robot, (j + 80, i))
        window.blit(robot, (j + 120, i))
        window.blit(robot, (j + 160, i))
        window.blit(robot, (j + 200, i))
        window.blit(robot, (j + 240, i))
        window.blit(robot, (j + 280, i))
        window.blit(robot, (j + 320, i))
        window.blit(robot, (j + 360, i))
        window.blit(robot, (j + 400, i))
        j += 10
        i += 20


pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()