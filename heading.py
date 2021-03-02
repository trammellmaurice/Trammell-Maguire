import math
import numpy as np


DESIRED_POS = (0,-2)

def head():
    # get current position
    curr_pos = (0,0,0)
    new_coord = (0,1)
    # CALCULATE UNIT VECTOR FOR CURRENT HEADING
    unit_vector = (round(math.cos(curr_pos[2])),math.sin(curr_pos[2]))
    # print(unit_vector)
    # CALCULATE VECTOR FROM CURRENT POSITION TO END POSITION (b-a)
    course = (DESIRED_POS[0]-curr_pos[0],DESIRED_POS[1]-curr_pos[1])
    # print(course)
    # FIND ANGLE BETWEEN TWO VECTORS
    angle = math.atan2(course[1],course[0]) - math.atan2(curr_pos[1],curr_pos[0])
    return angle

print(head())
