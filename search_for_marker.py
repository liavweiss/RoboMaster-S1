pid_x = rm_ctrl.PIDCtrl()
pid_y = rm_ctrl.PIDCtrl()
pid_Pitch = rm_ctrl.PIDCtrl()
pid_Yaw = rm_ctrl.PIDCtrl()
variable_X = 0
variable_Y = 0
variable_Post = 0
list_MarkerList = RmList()
pid = rm_ctrl.PIDCtrl()


# def vision_recognized_marker_trans_red_heart(msg):

#         led_ctrl.set_flash(rm_define.armor_all,2)

#         led_ctrl.set_top_led(rm_define.armor_top_all,255,0,0,rm_define.effect_flash)
#         led_ctrl.set_bottom_led(rm_define.armor_bottom_all,255,0,0,rm_define.effect_flash)
#         chassis_ctrl.stop()
#         time.sleep(1)

def recognize_marker():
    gimbal_ctrl.rotate_with_speed(270, 0.3)
    # chassis_ctrl.move_with_time(0,1)
    res = -1
    while res == -1:
        list_MarkerList = RmList(vision_ctrl.get_marker_detection_info())
        if list_MarkerList[1] == 1:
            res = list_MarkerList[2]
            print(res)
            # gimbal_ctrl.rotate_with_speed(-100,0.3)
            return res


def shoot_marker(marker):
    V_avg = 1
    k = 0.65
    print("befor")
    # time.sleep(5)
    gimbal_ctrl.rotate_with_speed(-50, 0.3)
    print("afetr")
    time.sleep(5)
    # chassis_ctrl.move_with_time(0,1)
    while True:
        print(marker)
        list_MarkerList = RmList(vision_ctrl.get_marker_detection_info())

        # vision_ctrl.cond_wait(rm_define.cond_recognized_marker_trans_red_heart)
        print(list_MarkerList)
        # list_MarkerList[1]=1
        # print("_______")
        if list_MarkerList[1] == 1 and list_MarkerList[2] == marker:
            print(list_MarkerList)
            print("xxxxx")
            robot_ctrl.set_mode(rm_define.robot_mode_chassis_follow)
            variable_x = list_MarkerList[4]
            # pid.set_error(variable_x - 0.5)
            # gimbal.rotate_with_speed(pid.get_output(),0)
            vision_ctrl.set_marker_detection_distance(1)
            v = (V_avg - (k * abs(list_MarkerList[3] / 180)))
            chassis_ctrl.set_trans_speed(v * 0.3)
            chassis_ctrl.move(0)

            variable_X = list_MarkerList[3]
            variable_Y = list_MarkerList[4]
            pid_Yaw.set_error(variable_X - 0.5)
            pid_Pitch.set_error(0.5 - variable_Y)
            vision_ctrl.set_marker_detection_distance(1)
            gimbal_ctrl.rotate_with_speed(pid_Yaw.get_output(), pid_Pitch.get_output())
            time.sleep(0.05)
            gun_ctrl.set_fire_count(1)
            gun_ctrl.fire_once()
            time.sleep(1)
            variable_Post = 0.01
            if abs(variable_X - 0.5) <= variable_Post and abs(0.5 - variable_Y) <= variable_Post:
                gun_ctrl.set_fire_count(1)
                gun_ctrl.fire_once()
                time.sleep(1)
        else:
            gimbal_ctrl.rotate_with_speed(0, 0)


def start():
    global variable_X
    global variable_Y
    global variable_Post
    global list_MarkerList
    global pid_x
    global pid_y
    global pid_Pitch
    global pid_Yaw
    robot_ctrl.set_mode(rm_define.robot_mode_free)
    vision_ctrl.enable_detection(rm_define.vision_detection_marker)
    pid_Yaw.set_ctrl_params(115, 0, 5)
    pid_Pitch.set_ctrl_params(85, 0, 3)
    chassis_ctrl.set_trans_speed(0.3)
    marker = recognize_marker()
    shoot_marker(marker)
    # chassis_ctrl.stop()
    # gimbal_ctrl.rotate_with_degree(rm_define.gimbal_up,5)