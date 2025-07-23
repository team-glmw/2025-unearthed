from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()
hub.system.set_stop_button([Button.RIGHT, Button.LEFT])

#hub.light.on(Color.BLUE)
#wait(2000)
#hub.light.on(Color.RED)
#while 1:
    #if(hub.buttons.pressed() == {Button.CENTER}):
        #break
#hub.light.on(Color.GREEN)
#wait(2000)

def set_speed(robot, speed):
    # settings = robot.settings()
    # robot.settings(speed, settings[1], settings[2], settings[3])
    robot.settings(straight_speed=872)

# robot.drive(speed, turn_rate)
# robot.stop()
# robot.angle()

MotorA = Motor(Port.A, Direction.COUNTERCLOCKWISE)
MotorB = Motor(Port.B)
robot = DriveBase(MotorA, MotorB, 50, 125)
robot.use_gyro(True)

set_speed(robot,1000)
robot.reset()


def precise_turn (target):
    while 1:
        closeness = target - robot.angle()
        robot.drive(0, closeness*100)
        if closeness < 0.20:
            robot.stop()
            break


precise_turn(40)
print("DONE: ", robot.angle())
exit()




robot.straight(80)
robot.turn(-65)
robot.straight(600)

robot.straight(-1000)

#turn(dest, deadband, veldeadband, p):
#    while abs(pos-dest) < deadband and vel < veldeadband:
#        speed = p * (pos-dest)

print("Distance = ", robot.distance())
print("Angle = ", robot.angle())