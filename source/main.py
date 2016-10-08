from direct.showbase.ShowBase import ShowBase
from direct.task.TaskManagerGlobal import taskMgr
from shapes.shapeGenerator import Cube, Sphere
from createMovement import *
from filters import *
from world import *
from player import *
from cameraSetup import *
from handleControls import *
from createLight import *

class Glyde(ShowBase):

    def __init__(self):
        ShowBase.__init__(self)
        self.make_controls()
        self.create_world()
        self.create_player_placeholder(1, 1, 1)
        self.setup_camera()
        self.add_filters()
        self.create_movement()
        self.add_light()

    def make_controls(self):
        self.controls = handleControls()
        print(self.controls.forward)

    def create_world(self):
        self.World = world()

    def create_player_placeholder(self, l, w, h):
        self.Player = player()
        
    def setup_camera(self):
        self.finishedCamera = cameraSetup(base.render.find("player"))

    def add_filters(self):
        self.filters = filters()

    def create_movement(self):
        self.movement = createMovement(taskMgr, self.World.worldSeed)

    def add_light(self):
        self.light = createLight("world", base.render.find('player'))


game = Glyde()
game.run()