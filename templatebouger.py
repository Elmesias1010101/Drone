#!/usr/bin/env python
from __future__ import print_function
​
import roslib
#roslib.load_manifest('my_package')
import sys
import rospy
import cv2
from std_msgs.msg import Empty
from geometry_msgs.msg import Twist
import time
​
​
​
​
class MoveDrone:
​
	def __init__(self):
​
		self.takeoff_pub = rospy.Publisher("TOPIC_NAME", Empty) # TODO put the takeoff topic name here
		self.landing_pub = rospy.Publisher("TOPIC_NAME", Empty) # TODO put the landing topic name here
​
		self.move_pub = rospy.Publisher("TOPIC_NAME", TWIST) # Publish commands to drone 
​
	def move_drone(self, speed=[0.0, 0.0, 0.0], orient=[0.0, 0.0, 0.0]):
​
		vel_msg = Twist()
​
		# TODO: fill the velocity fields here with the desired values
​
​
		# TODO: fill the angulare velocities here with the desired values
​
​
​
​
		self.move_pub.publish(vel_msg)
​
		return 0
​
​
​
	def takeoff_drone(self):
​
		empty_msg = Emtpy()
		
		# TODO: send takeoff command to the drone
​
​
​
​
	def land_drone(self):
​
		empty_msg = Emtpy()
​
		# TODO: send landing command to the drone
​
​
​
​
​
if __name__ == '__main__':
​
	rospy.init_node('basic_controller', anonymous=True)
​
	move = MoveDrone()
​
​
	# TODO define your timer and your sequential commands here !
