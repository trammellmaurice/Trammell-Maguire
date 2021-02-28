import rospy
import math
from turtleAPI import robot

def distance(start,fin):
    return math.sqrt(((fin[0]-start[0])**2)+((fin[1]-start[1])**2))

turtle = robot()

# initialize bot by getting world position
start_pos = turtle.getPositionTup()

# make bot drive
turtle.drive(0,5)

#check position loop
current_pos = turtle.getPositionTup()
while (start_pos,current_pos) < 5:
    current_pos = turtle.getPositionTup()

turtle.stop()
