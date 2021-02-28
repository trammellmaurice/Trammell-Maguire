import rospy
import math
from turtleAPI import robot
from pid import pidController

DESIRED_POS = (1,0,0)

"""
DISTANCE
Find distance between two points
"""
def distance(start,fin):
    return math.sqrt(((fin[0]-start[0])**2)+((fin[1]-start[1])**2))

"""
DISTANCE ERROR
Find the error in distance from current position to desired position
"""
def d_error(desired):
    return distance(turtle.getPositionTup(),desired)

"""
STEERING ERROR
Find the error in yaw
"""
def s_error(desired):
    # get current yaw
    current = turtle.getPositionTup()[2]
    #desired-current = error
    return (desired-current)

"""
LOCALIZE
Update all position and steering methods at once
"""
def update(desired_pos):
    # get error for yaw and update steering
    steering.update(s_error(desired_pos[2]))
    #d = d_error(desired_pos)

"""
CORRECT
Corrections from PID controllers
"""
def correct():
    return steering.pid()

"""
EXECUTION
"""
turtle = robot() # initialize robot

# PID CONTROLLER
steering = pidController(2) # make a p controller for steering with kp

# initialize bot by getting world position
update(turtle.getPositionTup())

# make bot drive
turtle.drive(0,0.25)

# position loop
while not rospy.is_shutdown():
    # get current position
    update(DESIRED_POS)
    turtle.drive(steering.pid(),0.25)


turtle.stop()
