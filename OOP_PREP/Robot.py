from IRobot import IRobot
class Robot(IRobot):
    def __init__(self, name):
        self.name = name
    
    def forward(self, steps):
        print("Basic robot: Moving forward {} steps beep boop".format(steps))

    def turn(self, direction, degrees):
        print("Basic robot: Turning {} {} degrees".format(direction, degrees))

    def beep(self, power, number_of_beeps):
        print("Basic robot: {}".format("beep "*number_of_beeps))
        
