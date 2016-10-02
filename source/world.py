from shapes.shapeGenerator import Cube, Sphere

class world():

    def __init__(self):
        self.create_dev_world(100, 100, 1)

    def create_dev_world(self, l, w, h):
        self.devWorldGeom = Cube(l, w, h)
        self.devWorldNode = base.render.attachNewNode("world")
        self.devWorldGeom.reparentTo(self.devWorldNode)