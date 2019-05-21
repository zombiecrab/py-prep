from IRobot import IRobot

class KillerRobot(IRobot):
    def __init__(self, name):
        self.name = name

    def forward(self, steps):
        print("KILLER ROBOT: Exsessive force in {} steps".format(steps))

    def turn(self, direction, degrees):
        print("KILLER ROBOT: Turning {} {} dregress to cook a fool".format(direction, degrees))
    
    def beep(self, power, number_of_beeps):
        print("KILLER_ROBOT: {}".format("DIE "*number_of_beeps))