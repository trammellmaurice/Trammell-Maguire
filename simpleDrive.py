import rospy
import math
import numpy as np
from turtleAPI import robot
from pid import pidController

#POSITIVE = COUNTER CLOCKWISE

DESIRED_POS = (2,0)
"""
HEADING
Calculate heading to get to point
"""
def head():
    # get current position
    curr_pos = turtle.getPositionTup()
    new_coord = (0,1)
    # CALCULATE UNIT VECTOR FOR CURRENT HEADING
    unit_vector = (round(math.cos(curr_pos[2])),math.sin(curr_pos[2]))
    # print(unit_vector)
    # CALCULATE VECTOR FROM CURRENT POSITION TO END POSITION (b-a)
    course = (DESIRED_POS[0]-curr_pos[0],DESIRED_POS[1]-curr_pos[1])
    # print(course)
    # FIND ANGLE BETWEEN TWO VECTORS
    # DO DOT PRODUCTS
    top = np.dot(unit_vector,course)
    # calculate magnitude
    unit_vector = math.sqrt(unit_vector[0]**2+unit_vector[1]**2)
    course = math.sqrt(course[0]**2+course[1]**2)
    diff = math.acos(top/(unit_vector*course))
    return diff

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
    steering.update(head())
    throttle.update(d_error(DESIRED_POS))
    return 0

"""
EXECUTION
"""
turtle = robot() # initialize robot

# PID CONTROLLERS
steering = pidController(10,1,2) # make a p controller for steering with just kp
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
        turtle.drive(steering.pid(),0)
        rospy.loginfo(turtle.getPositionTup())
        turtle.stop()
        break
