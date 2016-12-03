#!/usr/bin/env python

import cv2
import cv_bridge
import rospy
from sensor_msgs.msg import Image

i = 0


class Phototaker:
    def __init__(self):
        self.bridge = cv_bridge.CvBridge()
        self.image_sub = rospy.Subscriber('camera/rgb/image_raw', Image, self.image_callback)

    def image_callback(self, msg):
        image = self.bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8')
        cv2.imshow("image", image)
        # global i
        # i += 1
        # cv2.imwrite('/home/ming/' + str(i) + '.jpg', image)
        cv2.waitKey()


rospy.init_node('image_subscriber')
phototaker = Phototaker()
rospy.spin()
