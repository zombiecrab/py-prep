from Robot import Robot
from KillerRobot import KillerRobot
from RobotRecorder import RobotRecorder
from RobotPlayer import RobotPlayer

robot_a = Robot("Fabien")
robot_recorder_a = RobotRecorder(robot_a)

robot_recorder_a.forward(10)
robot_recorder_a.turn("RIGHT", 30)
robot_recorder_a.beep("HIGH", 20)

robot_b = KillerRobot("Tobias")
robot_recorder_b = RobotRecorder(robot_b)

robot_recorder_b.forward(50)
robot_recorder_b.turn("LEFT", 90)
robot_recorder_b.beep("MAX", 30)

print(robot_recorder_a.getActions())
print(robot_recorder_b.getActions())

player_a = RobotPlayer(robot_a)
player_a.runActions(robot_recorder_a.getActions())

player_b = RobotPlayer(robot_b)
player_b.runActions(robot_recorder_b.getActions())
