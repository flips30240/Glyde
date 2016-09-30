from direct.task.Task import Task as Task

class createMovement():

    def __init__(self, taskmanager):
        #self.shapeNode = base.render.find("shape")
        self.taskManager = taskmanager
        globalUpdate = Task(self.start_global_update)
        self.taskManager.add(globalUpdate, "global update")

    def start_global_update(self, task):
        return task.cont