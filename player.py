class Player:
    def __init__(self):
        self.pos = []
        self.angle = 0
        self.velocity = []
        self.isSitting = False
        self.isNearChair = False
        self.isDead = False

    def detect_chair(self):
        pass

    def sit(self):
        pass

    def event_handler(self):
        pass

    def draw(self, screen):
        pass

    def draw_character(self):
        pass

    def draw_death(self):
        pass
