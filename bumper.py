import rospy
import numpy
from turtleAPI import robot

try:
  print("creating robot")
  r= robot()
  while not rospy.is_shutdown():
      r.drive(0, .2)
      print r.getBumpStatus() # returns a tuple type
      if r.getBumpStatus().get('state') == 1:
          # bumper pressed, turn around
          if r.getBumpStatus().get('bumper') == -1:
              # back bumper
              while r.getAngle() is not numpy.pi/2:
                  r.drive(.2, 0)
              r.drive(0, .2)
          elif r.getBumpStatus().get('bumper') == 0:
              # left bumper
              while r.getAngle() is not numpy.pi/2:
                  r.drive(.2, 0)
              r.drive(0, .2)
          elif r.getBumpStatus().get('bumper') == 1:
              # forward bumper
              while r.getAngle() is not numpy.pi/2:
                  r.drive(.2, 0)
              r.drive(0, .2)
          elif r.getBumpStatus().get('bumper') == 2:
              # right bumper
              while r.getAngle() is not numpy.pi/2:
                  r.drive(.2, 0)
              r.drive(0, .2)

  r.stop()
except Exception as e:
  print(e)
  rospy.loginto("node now terminated")
