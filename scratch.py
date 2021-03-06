import math

import rospy
from turtleAPI import robot

from pid import pidController

#END = (-1,0) # test destination
# START = (0,0,3*(math.pi)/2) # test start

"""
FIND STEERING ERROR
Calculate steering error to get to point
"""
def steeringError():
    # get current position
    curr_pos = turtle.getPositionTup()
    # CALCULATE VECTOR FROM CURRENT POSITION TO END POSITION (b-a)
    course = (END[0]-curr_pos[0],END[1]-curr_pos[1])
    # print(course)
    # FIND ANGLE BETWEEN TWO VECTORS
    angle = math.atan2(course[1],course[0]) - curr_pos[2]
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
def distanceError():
    return distance(turtle.getPositionTup(),END)

"""
EXECUTION
"""

turtle = robot() # initialize robot

# PID CONTROLLERS
steering_controller = pidController(0.75) # make a p controller for steering with just kp
throttle_controller = pidController(0.5,0,0.5) # make a p controller for throttle with just kp

rate = rospy.Rate(20)

while not rospy.is_shutdown():
    # get input
    END = input()

    # get initial steering error to turn
    while abs(steeringError()) > 0.1: # turning loop
        steering_error = steeringError() # update steering error
        steering_controller.update(steering_error)
        rospy.loginfo(steering_error)
        turtle.drive(steering_controller.pid(),0) # just turn the right amount
        rate.sleep()
    turtle.stop()

    # get initial distance error to start moving
    while distanceError() > 0.01: # driving loop
        distance_error = distanceError()
        steering_error = steeringError()
        throttle_controller.update(distance_error)  # update distance error
        steering_controller.update(steering_error) # update steering error
        rospy.loginfo(distance_error)
        turtle.drive(steering_controller.pid(),throttle_controller.pid())
        rate.sleep()
    turtle.stop()
