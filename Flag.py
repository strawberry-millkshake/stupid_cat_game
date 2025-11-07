from Entity import Entity

class Flag(Entity):
    def __init__(self, level, pos_x, pos_y):
        super().__init__(level, 50, 50, pos_x, pos_y, 0, 0, "sprites/flag.jpg", 0, 0, 0)

        self.type = "flag"

    def update(self):
        self.entity_update()
        self.collision_physics()