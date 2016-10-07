from shapes.shapeGenerator import Cube, Sphere
import random
import math

class world():

    def __init__(self):
        self.create_dev_world(100, 100, 1)
        self.create_test_island()

    def create_dev_world(self, l, w, h):
        self.devWorldGeom = Cube(l, w, h)
        self.devWorldNode = base.render.attachNewNode("world")
        self.devWorldGeom.reparentTo(self.devWorldNode)

    def create_test_island(self):
        def determine_location():
            self.testIslandNode = base.render.attachNewNode("test island")
            self.testIslandNode.setPos(-50, 120, 0)
        def determine_bounds(min, max):
            self.bounds = random.randint(min, max)
        def determine_dimensions():
            self.width = self.bounds
            self.length = (self.width/random.randint(1, 3))
            self.length = int(((math.ceil(self.length/2))*2) + 1)
            if self.width >= self.length:
                self.height = self.length
            else:
                self.height = self.width
            print(self.width, self.length, self.height)
        def create_top():
            self.topGeom = Cube(self.width, self.length, 1)
            self.topGeom.setPos(0, 0, 0)
            self.topGeom.reparentTo(self.testIslandNode)
        def create_bottom():
            for z in range(self.height):
                testCube = Cube(self.width - z, self.length - z, 1)
                testCube.setPos(z/2, z/2, -z/2)
                testCube.reparentTo(self.testIslandNode)
            self.testIslandNode.flattenStrong()

        determine_location()
        determine_bounds(100, 1000)
        determine_dimensions()
        create_top()
        create_bottom()