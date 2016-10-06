from panda3d.core import *
class createLight():

    def __init__(self, str, nodepath):

        if str == "world":
            self.add_world_spotlight(nodepath)
            self.add_world_ambient_light()
        else:
            print("keyword " + str + " is not recognized!")

    def add_world_spotlight(self, nodeToFollow):
        self.worldLight = base.render.attachNewNode(DirectionalLight("world light"))
        #self.worldLight.node().setScene(base.render)
        self.worldLight.node().setShadowCaster(True, 512, 512)
        self.worldLight.node().showFrustum()
        self.worldLight.node().getLens().setFov(30)
        self.worldLight.node().getLens().setNearFar(30, 150)
        self.worldLight.node().getLens().setFilmSize(200)
        #self.worldLight.reparentTo(base.render.find("player"))
        self.worldLight.setPos(50, 0, 50)
        self.worldLight.lookAt(nodeToFollow)
        base.render.setLight(self.worldLight)

        base.render.setShaderAuto()

    def add_world_ambient_light(self):
        self.worldAmbLight = base.render.attachNewNode(AmbientLight("world ambient light"))
        self.worldAmbLight.node().setColor(VBase4(.2, .2, .2, 1))
        base.render.setLight(self.worldAmbLight)