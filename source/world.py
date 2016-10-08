from shapes.shapeGenerator import Cube, Sphere, Pyramid
import random
import math

class world():

    def __init__(self, seed = 0):
        if seed == 0:
            self.generate_random_seed()
        else:
            self.create_world(seed)
        #self.create_dev_world(50, 8)

    def generate_random_seed(self):
        self.worldSeed = random.randint(1, 9999999999)
        print(self.worldSeed)

    def create_dev_world(self, rad, sides):
        self.devWorldGeom = Pyramid(rad, sides)
        self.devWorldGeom.setR(180)
        self.devWorldNode = base.render.attachNewNode("world")
        self.devWorldGeom.reparentTo(self.devWorldNode)