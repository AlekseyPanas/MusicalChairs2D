import pygame
pygame.init()

screen = pygame.display.set_mode((700, 700), pygame.DOUBLEBUF)

running = True

while running:
    screen.fill((100, 100, 100))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()
