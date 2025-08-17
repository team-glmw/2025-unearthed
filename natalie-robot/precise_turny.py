from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()

motorA = Motor(Port.A, Direction.COUNTERCLOCKWISE)
motorB = Motor(Port.B)
base = DriveBase(motorA, motorB, 50, 135)
base.settings(800, 600, 600, 600)
base.use_gyro(True)
base.reset()

def cool_challenge():
    base.straight(400)
    base.turn(90)
    print(base.distance())
    print(base.angle())
    base.straight(150)
    base.turn(-90)
    print(base.distance())
    print(base.angle())
    base.straight(420)
    base.straight(-420)
    base.turn(45)
    base.straight(-700)

def precise_turny(angle):
    base.drive(0, 1000)
    while 1:
        if base.angle()>angle:
            base.stop()
            break

precise_turny(90)
print(base.angle())