import pygame

MENU = None
events = None
running = True


def start_app():
    global MENU, events
    MENU = None

    events = pygame.event.get()
