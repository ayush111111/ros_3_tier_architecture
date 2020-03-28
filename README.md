# ros_3_tier_architecture




1)Create 3 ROS nodes, the first node publishes a Name and corresponding age. The
name and age is considered one data packet, a respective ROS msg needs to be
created. This message should be subscribed to the second node, where it checks the
person’s eligibility to vote. If age >= 18, eligible voter; if age < 18, ineligible. Publish
the name and the eligibility status from this node to the third ROS node (create
another ROS msg for this part). In the third node, simply print the data subscribed.



ROS nodes ran in order 3-1-2


1. PTR:

  1.1 node_1
        ctrl_c = False

        while not ctrl_c:
            connections = pub.get_num_connections()
            if connections > 0 :
                pub.publish(message) 
                print('done')
                ctrl_c = True 
          
          
    Above code is used to publish message when connection between node1 and node2 is established
     
     
       
       
