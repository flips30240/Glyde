from shapes.shapeGenerator import Cube, Sphere

class player():

    def __init__(self):
        self.create_dev_player(1, 3, 10)

    def create_dev_player(self, l, w, h):
        self.PLayerGeom = Cube(l, w, h)
        self.PlayerNode = base.render.attachNewNode("player")
        self.PLayerGeom.reparentTo(self.PlayerNode)
