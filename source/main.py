from direct.showbase.ShowBase import ShowBase
from direct.task.TaskManagerGlobal import taskMgr
from shapes.shapeGenerator import Cube, Sphere
from createMovement import *

class Glyde(ShowBase):

    def __init__(self):
        ShowBase.__init__(self)

        self.create_cube(1, 1, 1)
        self.create_movement()

    def create_cube(self, l, w, h):
        self.shape = Cube(l, w, h)
        self.shapeNode = base.render.attachNewNode("shape")
        self.shape.reparentTo(self.shapeNode)
        self.shapeNode.setPos(0, 10, 0)

    def create_movement(self):
        movement = createMovement(taskMgr)


game = Glyde()
game.run()