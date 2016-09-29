from direct.task.Task import Task as Task

class createMovement():

    def __init__(self, taskmanager):
        self.taskManager = taskmanager
        print(base.render.getChild(1))
        self.shapeNode = base.render.getChild(1)
        testTask = Task(self.start_movement_task)
        self.taskManager.add(testTask, "shape mover")
        print(self.shapeNode.getX())

    def start_movement_task(self, task):
        self.shapeNode.setH(self.shapeNode.getH() + 1)
        self.shapeNode.setP(self.shapeNode.getP() - 1)
        self.shapeNode.setR(self.shapeNode.getR() + 3)
        return task.cont