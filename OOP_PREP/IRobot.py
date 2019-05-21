import abc

class IRobot(abc.ABC):
    @abc.abstractmethod
    def forward(steps):
        pass

    @abc.abstractmethod
    def turn(direction, degrees):
        pass

    @abc.abstractmethod
    def beep(power, number_of_beeps):
        pass