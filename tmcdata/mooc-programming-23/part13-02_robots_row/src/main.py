import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("src\\robot.png")

width = robot.get_width()
height = robot.get_height()

window.fill((0, 0, 0))

window.blit(robot, (40, 0))
window.blit(robot, (80, 0))
window.blit(robot, (120, 0))
window.blit(robot, (160, 0))
window.blit(robot, (200, 0))
window.blit(robot, (240, 0))
window.blit(robot, (280, 0))
window.blit(robot, (320, 0))
window.blit(robot, (360, 0))
window.blit(robot, (400, 0))


pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()