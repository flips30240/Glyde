import sys

class handleControls():

    def __init__(self):
        self.check_for_controls_file()
        self.parse_controls()
        self.handle_keystrokes()

    def check_for_controls_file(self):
        try:
            self.controlsFile = open("./settings/controls.txt")
            print("test")
        except:
            self.controlsFile = open("./settings/controls.txt", "w")
            print("hmm")

    def parse_controls(self):
        self.lines = self.controlsFile.readlines()

        for x in range(len(self.lines)):
            if self.lines[x].strip() == "forward":
                self.forward = self.lines[x+1].strip()
            if self.lines[x].strip() == "left":
                self.left = self.lines[x+1].strip()
            if self.lines[x].strip() == "right":
                self.right = self.lines[x+1].strip()
            if self.lines[x].strip() == "backward":
                self.backward = self.lines[x+1].strip()
            if self.lines[x].strip() == "jump":
                self.jump = self.lines[x+1].strip()
            if self.lines[x].strip() == "pause":
                self.pause = self.lines[x+1].strip()

        print(self.forward, self.backward, self.left, self.right, self.jump)

    def handle_keystrokes(self):
        self.movementCheckNode = base.render.attachNewNode("movement check")
        self.movementCheckNode.setPos(0, 0, 0)

        base.accept(self.forward, self.move, extraArgs=[self.forward])
        base.accept(self.forward+"-up", self.stop, extraArgs=[self.forward])

        base.accept(self.left, self.move, extraArgs=[self.left])
        base.accept(self.left+"-up", self.stop, extraArgs=[self.left])

        base.accept(self.backward, self.move, extraArgs=[self.backward])
        base.accept(self.backward+"-up", self.stop, extraArgs=[self.backward])

        base.accept(self.right, self.move, extraArgs=[self.right])
        base.accept(self.right+"-up", self.stop, extraArgs=[self.right])

        base.accept(self.jump, self.move, extraArgs=[self.jump])
        base.accept(self.jump+"-up", self.stop, extraArgs=[self.jump])

        base.accept(self.pause, self.pause_menu)

    def move(self, direction):
        if direction == "w":
            self.movementCheckNode.setY(1)
        if direction == "a":
            self.movementCheckNode.setX(-1)
        if direction == "s":
            self.movementCheckNode.setY(-1)
        if direction == "d":
            self.movementCheckNode.setX(1)
        if direction == "space":
            self.movementCheckNode.setZ(1)

        print(self.movementCheckNode.getPos())

    def stop(self, direction):
        if direction == "w":
            self.movementCheckNode.setY(0)
        if direction == "a":
            self.movementCheckNode.setX(0)
        if direction == "s":
            self.movementCheckNode.setY(0)
        if direction == "d":
            self.movementCheckNode.setX(0)
        if direction == "space":
            self.movementCheckNode.setZ(0)

        print(self.movementCheckNode.getPos())

    def pause_menu(self):
        print("Leaving Game!")
        #will eventually call up a menu class#
        sys.exit()