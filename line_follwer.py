#################################################################################################################
#                                           RoboMaster Project                                                  #
#                                                                                                               #
#                                   Amichai Kafka & Liav weiss & Omer Michael                                   #
#################################################################################################################

# In this part of the project we will present the ability of the robot to follow a line.
# In this code the robot will follow a red line, but you can easily change the color
# of the line that the robot is following using line_follow_color_<color> located on line 30.
# First we lower the gimbal to look at the floor and after that as soon as the robot detects the red line it will move towards it,
# we have chosen the speed of the robot to be slower so that the robot can make sharp turns.

pid=rm_ctrl.PIDCtrl()

def start():
    robot_ctrl.set_mode(rm_define.robot_mode_gimbal_follow)
    gimbal_ctrl.rotate_with_degree(rm_define.gimbal_down,20)
    vision_ctrl.enable_detection(rm_define.vision_detection_line)
    vision_ctrl.line_follow_color_set(rm_define.line_follow_color_red)
    media_ctrl.exposure_value_update(rm_define.exposure_value_small)
    V_avg=1
    k=0.65

    pid.set_ctrl_params(330,0,28)
    while True:
        LineList=RmList(vision_ctrl.get_line_detection_info())
        print(LineList)
        if len(LineList) == 42:
            if LineList[2] >= 1:
                robot_ctrl.set_mode(rm_define.robot_mode_chassis_follow)
                variable_x = LineList[19]
                pid.set_error(variable_x - 0.5)
                gimbal_ctrl.rotate_with_speed(pid.get_output(),0)
                v=(V_avg-(k*abs(LineList[37]/180)))
                chassis_ctrl.set_trans_speed(v*0.5)
                chassis_ctrl.move(0)
        else:
            gimbal_ctrl.rotate_with_speed(0,0)
            # chassis_ctrl.stop()