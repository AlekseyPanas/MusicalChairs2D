import pygame
import Constants
import Globe
pygame.init()

screen = pygame.display.set_mode(Constants.SCREEN_SIZE, pygame.DOUBLEBUF)

# Main game loop
while Globe.running:
    screen.fill((100, 100, 100))

    Globe.events = pygame.event.get()

    for event in Globe.events:
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()
