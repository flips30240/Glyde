class cameraSetup():

    def __init__(self, nodepathToFollow):
        base.disableMouse()
        self.parent_camera(nodepathToFollow)
        self.create_rotational_nodes(nodepathToFollow)
        base.accept("wheel_up", self.move_camera, extraArgs=[1])
        base.accept("wheel_down", self.move_camera, extraArgs=[-1])

    def parent_camera(self, nodepath):
        self.cameraNode = render.attachNewNode("camera node")
        base.cam.reparentTo(self.cameraNode)
        base.cam.setPos(0, -10, 10)
        base.cam.lookAt(nodepath)

    def create_rotational_nodes(self, nodepath):
        self.cameraHNode = render.attachNewNode("camera h node")
        self.cameraPNode = render.attachNewNode("camera p node")

    def move_camera(self, dist):
        base.cam.setY(base.cam.getY() + dist)
        base.cam.setZ(base.cam.getZ() - dist)