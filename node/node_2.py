#! /usr/bin/env python

import rospy
from ros_task_1.msg import msg1
from ros_task_1.msg import msg2

message2 = msg2()
def callback(msg):
  message2.name = msg.name
  if msg.age < 18 :
   message2.eligibility = "ineligible"
  elif msg.age >= 18 :
   message2.eligibility = "eligible"
  print msg

rospy.init_node('node_2')

sub = rospy.Subscriber('/topic_1',msg1, callback)

pub = rospy.Publisher('/topic_2', msg2, queue_size=1)

ctrl_c = False

while not ctrl_c:
    connections = pub.get_num_connections()
    if connections > 0 :
        pub.publish(message2) 
        print('done')
        ctrl_c = True 

rospy.spin()
