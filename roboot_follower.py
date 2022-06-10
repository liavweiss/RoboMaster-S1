#################################################################################################################
#                                           RoboMaster Project                                                  #
#                                                                                                               #
#                                   Amichai Kafka & Liav weiss & Omer Michael                                   #
#################################################################################################################

# In this part of the project we will present the robot's ability to track and shoot a robot.
# First we want to control the chassis the and gimbal manual, after that we will Enable detection of robot.
# We will set the gimbal rotation speed to the maximum possible, for fast object.
# We will set the travel mode to free mode so we can automatically rotate the gimbal.
# To truck after the robot we will need to save his previous possitions and his current position.
# After that as long as we recognize the robot we will track his location and shoot at him non-stop,
# as soon as the robot comes out of the robot's mediator of vision the robot will stop and wait (to use as little battery of the robot as possible).



def start():
    # Enable manual control of chassis and gimbal.
    chassis_ctrl.enable_stick_overlay()
    gimbal_ctrl.enable_stick_overlay()
    V_avg = 1
    k = 0.65
    pid = rm_ctrl.PIDCtrl()
    
    gimbal_ctrl.rotate_with_degree(rm_define.gimbal_up, 20)
    # Enable detection of S1 robots.
    vision_ctrl.enable_detection(rm_define.vision_detection_car)
    vision_ctrl.set_marker_detection_distance(2)
    

    # Fire one bead per trigger. This does not affect IR firing. 
    gun_ctrl.set_fire_count(1)
    
    # Set gimbal rotation speed to the maximum possible, for fast object
    # tracking.
    gimbal_ctrl.set_rotate_speed(540)
   
    # Set travel mode to free mode so we can automatically rotate the gimbal.
    robot_ctrl.set_mode(rm_define.robot_mode_free)

    # Keep track of the current and previous x and y possitions of the
    # detected robot.
    prevX = 0.0
    prevY = 0.0
    x = 0.0
    y = 0.0

    while True:
        # Get list of detected S1 robots.
        robotList=RmList(vision_ctrl.get_car_detection_info())
        if robotList[1] > 0:
            # We found at least one robot.
            robot_ctrl.set_mode(rm_define.robot_mode_chassis_follow)
            variable_x = robotList[4]
            pid.set_error(variable_x - 0.5)
            # gimbal.rotate_with_speed(pid.get_output(),0)
            v = (V_avg - (k * abs(robotList[3] / 180)))
            chassis_ctrl.set_trans_speed(v * 0.5)
            chassis_ctrl.move(0)
           
            # Cache previous x and y values.
            prevX = x
            prevY = y
            
            # Get coordinates to the center of the first
            # detected S1 robot. This will be our target.
            x = robotList[2]
            y = robotList[3]
           
            # Robot detection is currently too slow.
            if abs(x - prevX) < 0.03 and abs(y - prevY) < 0.03:
                # It does not look like we got new values. Get robot
                # info again.
                continue
            
            # Get current sight coordinates.
            sightInfo = media_ctrl.get_sight_bead_position()
            sightX = sightInfo[0]
            sightY = sightInfo[1]
            
            # Obtain Compute gimbal angle in relation to the chassis.
            yawAngle = gimbal_ctrl.get_axis_angle(rm_define.gimbal_axis_yaw)
            pitchAngle = gimbal_ctrl.get_axis_angle(rm_define.gimbal_axis_pitch)
            
            # Compute yaw and pitch angle offsets (i.e. how much we need to
            # move).
            yaw = 96 * (x - sightX)
            pitch = 54 * (sightY - y)
            
            if abs(yaw) > 2 or abs(pitch) > 2:
                # Point gimbal to target.
                try:
                    gimbal_ctrl.angle_ctrl(yawAngle + yaw, pitchAngle + pitch)
                except:
                    print("Fail")           
                # Fire!
                gun_ctrl.fire_once()
        else:
            chassis_ctrl.stop()