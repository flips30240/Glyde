from direct.task.Task import Task as Task
import math

class createMovement():

    def __init__(self, taskmanager):
        #self.shapeNode = base.render.find("shape")
        self.taskManager = taskmanager
        globalUpdate = Task(self.start_global_update)
        self.taskManager.add(globalUpdate, "global update")

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

        base.render.find("player").setP(base.render.find("camera p node").getP())
        base.render.find("player").setH(base.render.find("camera h node").getH())
        #END CAMERA


        base.render.find("player").setPos(base.render.find("player").getPos() + base.render.find('movement check').getPos())
        return task.cont