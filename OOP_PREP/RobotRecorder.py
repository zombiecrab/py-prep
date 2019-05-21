from collections import OrderedDict

from IRobot import IRobot

class RobotRecorder(IRobot):

    def __init__(self, robot):
        self.actions = OrderedDict()
        self.robot = robot

    def forward(self, steps):
        self.robot.forward(steps)
        self.actions["forward"] = [steps]

    def turn(self, direction, degrees):
        self.robot.turn(direction, degrees)
        self.actions["turn"] = [direction, degrees]

    def beep(self, power, number_of_beeps):
        self.robot.beep(power, number_of_beeps)
        self.actions["beep"] = [power, number_of_beeps]

    def getActions(self):
        return self.actions
