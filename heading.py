import math
import numpy as np
curr_pos = (0,0,math.pi/2)
new_coord = (0,1)
# CALCULATE UNIT VECTOR FOR CURRENT HEADING
unit_vector = (round(math.cos(curr_pos[2])),math.sin(curr_pos[2]))
# print(unit_vector)
# CALCULATE VECTOR FROM CURRENT POSITION TO END POSITION (b-a)
course = (new_coord[0]-curr_pos[0],new_coord[1]-curr_pos[1])
# print(course)
# FIND ANGLE BETWEEN TWO VECTORS
# DO DOT PRODUCTS
top = np.dot(unit_vector,course)
# calculate magnitude
unit_vector = math.sqrt(unit_vector[0]**2+unit_vector[1]**2)
course = math.sqrt(course[0]**2+course[1]**2)
diff = math.acos(top/(unit_vector*course))
print(diff)
