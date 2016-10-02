class cameraSetup():

    def __init__(self, nodepathToFollow):
        base.disableMouse()
        self.parent_camera(nodepathToFollow)
        self.create_rotational_nodes(nodepathToFollow)

    def parent_camera(self, nodepath):
        self.cameraNode = render.attachNewNode("camera node")
        base.cam.reparentTo(self.cameraNode)
        base.cam.setPos(0, -10, 10)
        base.cam.lookAt(nodepath)

    def create_rotational_nodes(self, nodepath):
        self.cameraHNode = render.attachNewNode("camera h node")
        self.cameraPNode = render.attachNewNode("camera p node")