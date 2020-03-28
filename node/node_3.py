#! /usr/bin/env python

import rospy

from ros_task_1.msg import msg2

def callback(msg):
  print msg

rospy.init_node('node_3')

sub = rospy.Subscriber('/topic_2',msg2, callback)

rospy.spin()
