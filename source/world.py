from shapes.shapeGenerator import Cube, Sphere, Pyramid
import random
import math
import re

class world():

    def __init__(self, seed = 0):
        if seed == 0:
            self.generate_random_seed()
        else:
            self.create_world(seed)
        #self.create_dev_world(50, 8)

    def generate_random_seed(self):
        self.worldSeed = random.randint(1, 9999999999)
        print("original Seed = " + str(self.worldSeed))
        tempSeedStr = str(self.worldSeed)
        tempSeedArray = []
        for x in tempSeedStr:
            tempSeedArray.append(int(x))
        for x in range(len(tempSeedArray)):
            if tempSeedArray[x] == 0:
                tempSeedArray[x] = 3
        finalSeedStr = str(tempSeedArray)
        self.worldSeed = int(re.sub("[^0-9]", "", finalSeedStr))
        print("final world seed = " + str(self.worldSeed))

    def create_dev_world(self, rad, sides):
        self.devWorldGeom = Pyramid(rad, sides)
        self.devWorldGeom.setR(180)
        self.devWorldNode = base.render.attachNewNode("world")
        self.devWorldGeom.reparentTo(self.devWorldNode)