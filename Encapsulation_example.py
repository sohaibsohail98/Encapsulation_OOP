class Car:
    __maximum_speed = 0
    __name = ""

    def __init__(self):
        self.__maximum_speed = 200
        self.__name = "Supercar"

    def drive(self):
        print('driving. maxspeed ' + str(self.__maximum_speed))

    def setMaxSpeed(self, speed):
        self.__maximum_speed = speed


redcar = Car()
redcar.drive()
redcar.setMaxSpeed(374)
redcar.drive()