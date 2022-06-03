robot=robot_ctrl
gimbal=gimbal_ctrl
chassis=chassis_ctrl
media=media_ctrl
vision=vision_ctrl
armor=armor_ctrl
led=led_ctrl
define=rm_define

pid=rm_ctrl.PIDCtrl()

def start():
    # robot.set_mode(rm_define.robot_mode_gimbal_follow)
    # gimbal_ctrl.rotate_with_degree(rm_define.gimbal_down,20)
    # vision_ctrl.enable_detection(rm_define.vision_detection_line)
    robot.set_mode(define.robot_mode_gimbal_follow)
    gimbal.rotate_with_degree(define.gimbal_down,20)
    vision.enable_detection(define.vision_detection_line)
    vision.line_follow_color_set(define.line_follow_color_red)
    # vision.set_marker_detection_distance(1)
    media_ctrl.exposure_value_update(rm_define.exposure_value_small)
    V_avg=1
    k=0.65

    pid.set_ctrl_params(330,0,28)
    while True:
        # vision_ctrl.cond_wait(rm_define.cond_recognized)
        LineList=RmList(vision_ctrl.get_line_detection_info())
        print(LineList)
        if len(LineList) == 42:
            if LineList[2] >= 1:
                robot_ctrl.set_mode(define.robot_mode_chassis_follow)
                variable_x = LineList[19]
                pid.set_error(variable_x - 0.5)
                gimbal.rotate_with_speed(pid.get_output(),0)
                v=(V_avg-(k*abs(LineList[37]/180)))
                chassis.set_trans_speed(v*0.5)
                chassis.move(0)
        else:
            gimbal.rotate_with_speed(0,0)
            # chassis_ctrl.stop()