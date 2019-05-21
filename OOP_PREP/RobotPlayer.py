class RobotPlayer:
    def __init__(self, robot):
        self.robot = robot

    
    def runActions(self, actions):
        for action, params in actions.items():
            print("{}:{}".format(action, params))
            getattr(self.robot, action)(*params)