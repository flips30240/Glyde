from shapes.shapeGenerator import Cube, Sphere

class player():

    def __init__(self):
        self.create_dev_player(1, 3, 10)

    def create_dev_player(self, l, w, h):
        self.devPLayerGeom = Cube(l, w, h)
        self.devPlayerNode = base.render.attachNewNode("dev player")
        self.devPLayerGeom.reparentTo(self.devPlayerNode)