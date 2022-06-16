#################################################################################################################
#                                           RoboMaster Project                                                  #
#                                                                                                               #
#                                   Amichai Kafka & Liav weiss & Omer Michael                                   #
#################################################################################################################

# In this part of the project we will present the robot's ability to track and shoot a person.
# First we want to control the chassis the and gimbal manual, after that we will Enable detection of persons.
# We will set the gimbal rotation speed to the maximum possible, for fast object.
# We will set the travel mode to free mode so we can automatically rotate the gimbal.
# To truck after the persom we will need to save his previous possitions and his current position.
# After that as long as we recognize the human we will track his location and shoot at him non-stop,
# as soon as the person comes out of the robot's mediator of vision the robot will stop and wait (to use as little battery of the robot as possible).

pid = rm_ctrl.PIDCtrl()
pid_Pitch = rm_ctrl.PIDCtrl()
pid_Yaw = rm_ctrl.PIDCtrl()


def start():
    # Enable manual control of chassis and gimbal and free travel mode.
    chassis_ctrl.enable_stick_overlay()
    gimbal_ctrl.enable_stick_overlay()
    robot_ctrl.set_mode(rm_define.robot_mode_free)
    V_avg = 1
    k = 0.65
    gun_ctrl.set_fire_count(1)
    # Enable detection of persons.
    vision_ctrl.enable_detection(rm_define.vision_detection_people)
    vision_ctrl.set_marker_detection_distance(1)

    gimbal_ctrl.set_rotate_speed(540)
    pid.set_ctrl_params(330, 0, 28)
    pid_Yaw.set_ctrl_params(330, 0, 28)
    pid_Pitch.set_ctrl_params(330, 0, 28)

    x = 0.0
    y = 0.0

    while True:
        # Get list of detected persons.
        person_list = RmList(vision_ctrl.get_people_detection_info())
        if person_list[1] > 0:

            # We found at least one person.
            robot_ctrl.set_mode(rm_define.robot_mode_chassis_follow)
            chassis_ctrl.set_trans_speed(0.3)
            chassis_ctrl.move(0)
            # Keep track of the current and previous x and y possitions of the
            # detected person.
            prevX = x
            prevY = y

            # Get coordinates to the center of the first detected person.
            x = person_list[2]
            y = person_list[3]

            #if the targate close to the prev position continue
            if abs(x - prevX) < 0.03 and abs(y - prevY) < 0.03:
                continue

            print('x=', x, 'y=', y)

            # Obtain Compute gimbal angle in relation to the chassis.
            yaw_angle = gimbal_ctrl.get_axis_angle(rm_define.gimbal_axis_yaw)
            pitch_angle = gimbal_ctrl.get_axis_angle(rm_define.gimbal_axis_pitch)

            # Compute yaw and pitch angle offsets how much we need to move.
            yaw = 100 * (x - 0.5)
            pitch = 50 * (0.5 - y)
            print('yaw=', yaw, 'pitch=', pitch)
            # pid_Yaw.set_error(x - 0.5)
            # pid_Pitch.set_error(0.5 - y)
            if abs(yaw) > 2 or abs(pitch) > 2:
                # Point gimbal to target.
                gimbal_ctrl.angle_ctrl(yaw_angle + yaw, pitch_angle + pitch)
                gun_ctrl.fire_once()
        else:
            # gimbal.rotate_with_speed(0,0)
            chassis_ctrl.stop()