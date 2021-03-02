import math
import numpy as np
from turtleAPI import robot

DESIRED_POS = (2,0)

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

turtle = robot() # initialize robot
print(head())
