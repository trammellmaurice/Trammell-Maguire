import math

import rospy
from turtleAPI import robot

# get input
END = input()
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
EXECUTION
"""

turtle = robot() # initialize robot

rate = rospy.Rate(10)

while not rospy.is_shutdown():
    steering_error = steeringError()
    rospy.loginfo(steering_error)
    while abs(steering_error) > 0.1:
        if steering_error > 0:
            turtle.drive(0.25,0)
        elif steering_error < 0:
            turtle.drive(-0.25,0)
        rate.sleep()
    turtle.stop()
