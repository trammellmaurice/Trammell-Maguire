import rospy
import math
import numpy as np
from turtleAPI import robot
from pid import pidController

#POSITIVE = COUNTER CLOCKWISE

DESIRED_POS = (0,2)
"""
HEADING
Calculate heading to get to point
"""
def head():
    # get current position
    curr_pos = turtle.getPositionTup()
    # CALCULATE UNIT VECTOR FOR CURRENT HEADING
    unit_vector = (math.cos(math.round(curr_pos[2])),math.sin(math.round(curr_pos[2])))
    # print(unit_vector)
    # CALCULATE VECTOR FROM CURRENT POSITION TO END POSITION (b-a)
    course = (DESIRED_POS[0]-curr_pos[0],DESIRED_POS[1]-curr_pos[1])
    # print(course)
    # FIND ANGLE BETWEEN TWO VECTORS
    angle = math.atan2(course[1],course[0]) - math.atan2(curr_pos[1],curr_pos[0])
    return angle

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
def d_error():
    return distance(turtle.getPositionTup(),DESIRED_POS)

"""
EXECUTION
"""
turtle = robot() # initialize robot

# PID CONTROLLERS
steering = pidController(0.25) # make a p controller for steering with just kp
throttle = pidController(0.5) # make a p controller for throttle with just kp

# position loop
while not rospy.is_shutdown():
    # turning phase
    while abs(head()) > 0.02:
        steering.update(head())
        # turtle.drive(steering.pid(),0)
        print(head())
        print(steering.pid())
    turtle.stop()
    while d_error() > 0.02:
        throttle.update(d_error())
        steering.update(head())
        # print(steering.pid())
        # print(throttle.pid())
    #     # make bot drive based on error from pid controllers
    #     turtle.drive(round(steering.pid()),(throttle.pid()))
    turtle.stop()
    break
