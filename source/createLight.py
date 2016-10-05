from panda3d.core import *
class createLight():

    def __init__(self, str, nodepath):

        if str == "world":
            self.add_world_spotlight(nodepath)
        else:
            print("keyword " + str + " is not recognized!")

    def add_world_spotlight(self, nodeToFollow):
        self.worldSLight = base.render.attachNewNode(DirectionalLight("world spotlight"))
        #self.worldSLight.node().setScene(base.render)
        self.worldSLight.node().setShadowCaster(True, 1024, 1024)
        self.worldSLight.node().showFrustum()
        #self.worldSLight.node().getLens().setFov(30)
        self.worldSLight.node().getLens().setNearFar(1, 400)
        self.worldSLight.node().getLens().setFilmSize(50)
        #self.worldSLight.reparentTo(base.render.find("player"))
        self.worldSLight.setPos(50, 0, 50)
        self.worldSLight.lookAt(nodeToFollow)
        base.render.setLight(self.worldSLight)

        base.render.setShaderAuto()