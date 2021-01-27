#!/usr/bin/env python
from __future__ import print_function

import roslib
#roslib.load_manifest('my_package')
import sys
import rospy
import cv2
import numpy as np
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError

class image_converter:

  def __init__(self):

    #self.image_pub = rospy.Publisher("image_topic_2",Image)

    self.bridge = CvBridge()

    self.image_sub = rospy.Subscriber("/ardrone/front/image_raw",Image,self.callback)

  def callback(self,data):

    try:
      cv_image = self.bridge.imgmsg_to_cv2(data, "bgr8")
    except CvBridgeError as e:
      print(e)
    
    #print("im :\n",cv_image,'\n')
    #print("shape :\n",cv_image.shape,'\n')

    face_classifier = cv2.CascadeClassifier('/home/corentin/drone_workspace/src/my_package/scripts/haarcascade_frontalface_default.xml')

    gray = cv2.cvtColor(cv_image, cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray, 1.1, 4)

    #if faces is ():
       #print("No Face Found")
    for (x,y,w,h) in faces:
       cv2.rectangle(cv_image,(x,y),(x+w,y+h),(127,0,255),2)
       print("width : {} height : {}".format(w,h))
       cv2.imshow("Image window", cv_image)
       cv2.waitKey(1)


def main(args):
  ic = image_converter()
  rospy.init_node('image_converter', anonymous=True)
  try:
    rospy.spin()
  except KeyboardInterrupt:
    print("Shutting down")
  cv2.destroyAllWindows()

if __name__ == '__main__':
    main(sys.argv)
