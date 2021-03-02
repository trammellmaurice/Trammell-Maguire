import rospy
import time
import numpy
from turtleAPI import robot

try:
  print("creating robot")
  r= robot()
  while not rospy.is_shutdown():
      r.drive(0, .5)
      print r.getBumpStatus() # returns a tuple type
      print(r.getAngle()[2])
      if r.getBumpStatus().get('state') == 1:
          # bumper pressed, turn around
          # r.stop()
          print(r.getBumpStatus())
          print(r.getAngle()[2])
          if r.getBumpStatus().get('bumper') == 1:
              # back bumper
              while round(r.getAngle()[2], 1) != 1.6:
                r.drive(.5, 0)
              r.drive(0, .5)
          elif r.getBumpStatus().get('bumper') == 2:
              # left bumper
              while (round(r.getAngle()[2], 1) != -0.8 or round(r.getAngle()[2], 2) != 2.36):
                  r.drive(.5, 0)
              r.drive(0, .5)
          elif r.getBumpStatus().get('bumper') == -1:
              # forward bumper
              while round(r.getAngle()[2], 0) != 0:
                  r.drive(.5, 0)
              r.drive(0, .5)
          elif r.getBumpStatus().get('bumper') == 0:
              # right bumper
              while (round(r.getAngle()[2], 2) != -2.36 or round(r.getAngle()[2], 1) != 0.8):
                  r.drive(0.5, 0)
              r.drive(0, .5)
 # r.stop()
except Exception as e:
  print(e)
  rospy.loginto("node now terminated")
