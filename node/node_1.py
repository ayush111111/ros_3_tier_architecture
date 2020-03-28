#! /usr/bin/env python

import rospy
from ros_task_1.msg import msg1

rospy.init_node('node_1')

message = msg1()
message.name = "ayshh"
message.age = 18

pub = rospy.Publisher('/topic_1', msg1, queue_size=1)

ctrl_c = False

while not ctrl_c:
    connections = pub.get_num_connections()
    if connections > 0 :
        pub.publish(message) 
        print('done')
        ctrl_c = True 
 
