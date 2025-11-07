from Entity import Entity

class Cookie(Entity):
    def __init__(self, level, pos_x, pos_y):
        super().__init__(level, 50, 50, pos_x, pos_y, 0, 0, "sprites/cookie.jpg", 1.5, 0, 0)
        self.type = "cookie"

    def update(self):
        self.entity_update()
        self.collision_physics()