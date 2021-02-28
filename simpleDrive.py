import rospy
import math
from turtleAPI import robot
from pid import pidController
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

turtle = robot() # initialize robot
steering = pidController(2) # make a p controller for steering with kp



# initialize bot by getting world position
start_pos = turtle.getPositionTup()

# make bot drive
turtle.drive(0,5)

# position loop
while not rospy.is_shutdown():
    # get current position
    current_pos = turtle.getPositionTup()
    # check distance driven
    if distance(start_pos,current_pos) > 5:
        break # stop at correct distance

turtle.stop()
