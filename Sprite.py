import pygame


class Object:
    def __init__(self, lifetime, z_order, tags):
        self.lifetime = lifetime
        self.kill = False

        # Draw order
        self.z_order = z_order

        # Set of string tags that can identify an object
        self.tags = set(tags)

    @staticmethod
    def center_rotate(image, rect, angle):
        """Rotate the image while keeping its center."""
        # Rotate the original image without modifying it.
        new_image = pygame.transform.rotate(image, angle)
        # Get a new rect with the center of the old rect.
        rect = new_image.get_rect(center=rect.center)
        return new_image, rect

    def run_sprite(self, screen, is_draw, is_update):
        pass


# Class that manages any playable character in game
class Player(Object):
    def __init__(self, lifetime, z_order, tags):
        super().__init__(lifetime, z_order, tags)


# Class that implements user controls to the Player class
class UserPlayer(Player):
    def __init__(self, lifetime, z_order, tags):
        super().__init__(lifetime, z_order, tags)


# Class that implements AI Controls to the Player class
class AIPlayer(Player):
    def __init__(self, lifetime, z_order, tags):
        super().__init__(lifetime, z_order, tags)


class Chair(Object):
    def __init__(self, lifetime, z_order, tags):
        super().__init__(lifetime, z_order, tags)
