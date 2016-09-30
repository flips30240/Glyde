from direct.showbase.ShowBase import ShowBase
from direct.task.TaskManagerGlobal import taskMgr
from shapes.shapeGenerator import Cube, Sphere
from createMovement import *
from filters import *
from world import *
from player import *

class Glyde(ShowBase):

    def __init__(self):
        ShowBase.__init__(self)

        self.create_world_placeholder(100, 100, 1)
        self.create_player_placeholder(1, 1, 1)
        self.add_filters()
        self.create_movement()

    def create_world_placeholder(self, l, w, h):
        self.tempWorld = world()

    def create_player_placeholder(self, l, w, h):
        self.tempPlayer = player()

    def add_filters(self):
        self.filters = filters()

    def create_movement(self):
        self.movement = createMovement(taskMgr)


game = Glyde()
game.run()