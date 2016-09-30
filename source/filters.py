from direct.filter.CommonFilters import CommonFilters
from pandac.PandaModules import Material, Texture, TextureStage
from panda3d.core import Shader

class filters():

    def __init__(self):

        self.add_cartoon_ink()

    def add_cartoon_ink(self):

        self.filters = CommonFilters(base.win, base.cam)
        self.filters.setCartoonInk(separation = -1)