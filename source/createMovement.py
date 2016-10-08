from direct.task.Task import Task as Task
import math
from shapes.shapeGenerator import *

class createMovement():

    def __init__(self, taskmanager, seed):
        self.chunkNum = 0
        self.worldSeed = seed
        self.taskManager = taskmanager
        self.globalUpdate = Task(self.start_global_update)
        self.taskManager.add(self.globalUpdate, "global update")

    def start_global_update(self, task):

        #CAMERA
        pointer = base.win.getPointer(0)
        pointerX = pointer.getX()
        pointerY = pointer.getY()

        base.render.find("camera node").setPos(base.render.find("player").getPos())
        base.render.find("camera h node").setPos(base.render.find("player").getPos())
        base.render.find("camera p node").setPos(base.render.find("player").getPos())
        base.render.find("camera node").setH(base.render.find("camera h node").getH())
        base.render.find("camera node").setP(base.render.find("camera p node").getP())

        if base.win.movePointer(0, base.win.getXSize()/2, base.win.getYSize()/2):
            Pitch = -((pointerY - base.win.getYSize()/2)*.1)
            Heading = -((pointerX - base.win.getXSize()/2)*.1)

        base.render.find("camera p node").setP(base.render.find("camera p node"), Pitch)
        base.render.find("camera h node").setH(base.render.find("camera h node"), Heading)

        #base.render.find("player").setP(base.render.find("camera p node").getP())
        #will use later when if:in air
        base.render.find("player").setH(base.render.find("camera h node").getH())
        #END CAMERA

        #WORLD LIGHT MOVEMENT
        base.render.find("world light").setPos(base.render.find("player").getPos() + (50, 0, 50))
        #END WORLD LIGHT MOVEMENT

        #CONTROLS
        if base.render.find("movement check").getY() == 1:
            base.render.find("player").setY(base.render.find("player").find("move y node pos").getY(base.render))
            base.render.find("player").setX(base.render.find("player").find("move y node pos").getX(base.render))
        if base.render.find("movement check").getY() == -1:
            base.render.find("player").setY(base.render.find("player").find("move y node neg").getY(base.render))
            base.render.find("player").setX(base.render.find("player").find("move y node neg").getX(base.render))
        if base.render.find("movement check").getX() == 1:
            base.render.find("player").setY(base.render.find("player").find("move x node pos").getY(base.render))
            base.render.find("player").setX(base.render.find("player").find("move x node pos").getX(base.render))
        if base.render.find("movement check").getX() == -1:
            base.render.find("player").setY(base.render.find("player").find("move x node neg").getY(base.render))
            base.render.find("player").setX(base.render.find("player").find("move x node neg").getX(base.render))
        #END CONTROLS

        #WORLD GENERATION
        playerX = base.render.find("player").getX()
        playerY = base.render.find("player").getY()
        playerZ = base.render.find("player").getZ()
        if math.fabs(playerX) >= self.chunkNum * 1000:
            self.load_chunk()
        if math.fabs(playerY) >= self.chunkNum * 1000:
            self.load_chunk()
        if math.fabs(playerZ) >= self.chunkNum * 1000:
            self.load_chunk()
        return task.cont

    def load_chunk(self):
        testPyramid = Pyramid(100, 6)
        testPyramid.setR(180)
        testPyramid.setPos(base.render.find("player").getPos())
        testPyramid.reparentTo(base.render)
        self.chunkNum += 1