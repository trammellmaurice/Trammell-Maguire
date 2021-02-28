import rospy
import math
from turtleAPI import robot
from pid import pidController

#POSITIVE = COUNTER CLOCKWISE

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
UPDATE
Update all position and steering methods at once
"""
def update():
    # get error for yaw and update steering
    steering.update(s_error(DESIRED_POS[2]))
    throttle.update(d_error(DESIRED_POS))

"""
CORRECT
Corrections from PID controllers
"""
def correct():
    return (steering.pid(),throttle.pid())

"""
EXECUTION
"""
turtle = robot() # initialize robot

# PID CONTROLLERS
steering = pidController(10) # make a p controller for steering with just kp
throttle = pidController(0.5) # make a p controller for throttle with just kp

# position loop
while not rospy.is_shutdown():
    # get current position
    update()
    # print(steering.pid())
    #print(throttle.pid())
    # make bot drive based on error from pid controllers
    turtle.drive(steering.pid(),throttle.pid())
    if distance(turtle.getPositionTup(),DESIRED_POS) < 0.02:
        turtle.stop()
