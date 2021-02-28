import rospy
from turtleAPI import robot

rate = rospy.Rate(10)

turtle = robot()

# initialize bot by getting world position
start_pos = turtle.getPositionTup()

# make bot drive
turtle.drive(0,5)

rate.sleep()

#check position loop
current_pos = turtle.getPositionTup()
while current_pos-start_pos < 5:
    rate.sleep()
    current_pos = turtle.getPositionTup()

turtle.stop()
