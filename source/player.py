from shapes.shapeGenerator import Cube, Sphere

class player():

    def __init__(self):
        self.create_dev_player(1, 3, 10)

    def create_dev_player(self, l, w, h):
        self.PLayerGeom = Cube(l, w, h)
        self.PlayerNode = base.render.attachNewNode("player")
        self.PLayerGeom.reparentTo(self.PlayerNode)

        self.moveYNodePos = base.render.attachNewNode("move y node pos")
        self.moveYNodePos.reparentTo(self.PlayerNode)
        self.moveYNodePos.setPos(0, 1, 0)

        self.moveYNodeNeg = base.render.attachNewNode("move y node neg")
        self.moveYNodeNeg.reparentTo(self.PlayerNode)
        self.moveYNodeNeg.setPos(0, -1, 0)

        self.moveXNodePos = base.render.attachNewNode("move x node pos")
        self.moveXNodePos.reparentTo(self.PlayerNode)
        self.moveXNodePos.setPos(1, 0, 0)

        self.moveXNodeNeg = base.render.attachNewNode("move x node neg")
        self.moveXNodeNeg.reparentTo(self.PlayerNode)
        self.moveXNodeNeg.setPos(-1, 0, 0)
