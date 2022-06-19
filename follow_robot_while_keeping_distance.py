
#################################################################################################################
#                                           RoboMaster Project                                                  #
#                                                                                                               #
#                                   Amichai Kafka & Liav weiss & Omer Michael                                   #
#################################################################################################################

# This program allow robomaster to track other robot while keeping distance from it.
# When the robot identify other robot it measures the distance from it, that's done using the know height and the
# relative height that robomaster see of this robot.
# According to the distance robomaster advances to the robot or moves away from the robot

def start():
    # enable detection of S1 robots.
    vision_ctrl.enable_detection(rm_define.vision_detection_car)
    # vision_ctrl.set_marker_detection_distance(4)
    # gimbal_ctrl.rotate_with_degree(rm_define.gimbal_up,20)

    gimbal_ctrl.set_rotate_speed(540)
    # gimbal_ctrl.set_rotate_speed(60)

    chassis_ctrl.enable_stick_overlay()
    gimbal_ctrl.enable_stick_overlay()
    robot_ctrl.set_mode(rm_define.robot_mode_free)

    while True:


def distance_in_meter(height):
    return (270.0 / height) / 1000


def vision_recognized_car(msg):

    pid_pitch = None
    pid_yaw = None

    pid_pitch = rm_ctrl.PIDCtrl()
    pid_yaw = rm_ctrl.PIDCtrl()

    # pid parameters.
    pid_pitch.set_ctrl_params(90, 0, 3)
    pid_yaw.set_ctrl_params(120, 0, 5)

    while True:
        robot_list = vision_ctrl.get_car_detection_info()

        print("detected ", robot_list[0], "robot")

        if robot_list is None or robot_list[0] == 0:
            chassis_ctrl.stop()
            break

        distance = 0.0
        distance = distance_in_meter(robot_list[4])

        robot_ctrl.set_mode(rm_define.robot_mode_chassis_follow)
        print('robot is in', distance, ' meters away.')
        if distance > 0.8:
            #        # robot_ctrl.set_mode(rm_define.robot_mode_chassis_follow)
            #        # gimbal.rotate_with_speed(pid.get_output(),0)
            chassis_ctrl.set_trans_speed(0.5)
            chassis_ctrl.move(0)
        elif distance < 0.5:
            chassis_ctrl.set_trans_speed(0.5)
            chassis_ctrl.move(180)

        else:
            chassis_ctrl.stop()

        x = robot_list[1] - 0.5
        y = 0.5 - robot_list[2]

        if abs(x) <= 0.1 and abs(y) <= 0.1:
            gimbal_ctrl.rotate_with_speed(0, 0)

            return 2

        # Set error of the PID .
        pid_yaw.set_error(x)
        pid_pitch.set_error(y)

        gimbal_ctrl.rotate_with_speed(pid_yaw.get_output(), pid_pitch.get_output())