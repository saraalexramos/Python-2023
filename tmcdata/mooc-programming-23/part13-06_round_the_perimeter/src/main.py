# # WRITE YOUR SOLUTION HERE:
import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("src\\robot.png")

x = 0
y = 0
x_velocity = 1
y_velocity = 0
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    window.fill((0, 0, 0))
    window.blit(robot, (x, y))
    pygame.display.flip()
    
    x += x_velocity
    y += y_velocity

    if x_velocity > 0 and x + robot.get_width() >= 640:
        x_velocity = 0
        y_velocity = 1
    elif y_velocity > 0 and y + robot.get_height() >= 480:
        x_velocity = -1
        y_velocity = 0
    elif x_velocity < 0 and x <= 0:
        x_velocity = 0
        y_velocity = -1
    elif y_velocity < 0 and y <= 0:
        x_velocity = 1
        y_velocity = 0

    clock.tick(300)