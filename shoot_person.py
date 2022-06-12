#################################################################################################################
#                                           RoboMaster Project                                                  #
#                                                                                                               #
#                                   Amichai Kafka & Liav weiss & Omer Michael                                   #
#################################################################################################################

# In this part of the project we will present the robot's ability to fire his blaster every time he sees a person.
# Set the vision marker detection distance from 0.5 to 3 for farther distances.

def start():
    led1, led2 = 255, 100
    blink_rate = 6, 8

    # Blaster fire example function:

    def blaster_fire_example():

        robot_ctrl.set_mode(rm_define.robot_mode_chassis_follow)

        vision_ctrl.enable_detection(rm_define.vision_detection_people)
        vision_ctrl.set_marker_detection_distance(1)

        led_ctrl.set_top_led(rm_define.armor_top_all, led2, led2, led1, rm_define.effect_breath)
        led_ctrl.set_bottom_led(rm_define.armor_bottom_all, led2, led2, 1, rm_define.effect_breath)

        while True:
            vision_ctrl.cond_wait(rm_define.cond_recognized_people)
            chassis_ctrl.move_with_time(0, 1)
            while True:
                # chassis_ctrl.move_with_time(0,1)
                # vision_ctrl.detect_marker_and_aim(rm_define.marker_trans_target)
                randgimbal_speed = random.randint(20, 100)
                randup = random.randint(1, 55)

                gimbal_ctrl.set_rotate_speed(randgimbal_speed)

                media_ctrl.play_sound(rm_define.media_sound_gimbal_rotate, wait_for_complete_flag=False)

                led_ctrl.set_flash(rm_define.armor_all, blink_rate[0])
                led_ctrl.set_top_led(rm_define.armor_top_all, led2, led1, led1, rm_define.effect_marquee)
                led_ctrl.set_bottom_led(rm_define.armor_bottom_all, led2, led1, led1, rm_define.effect_flash)

                gimbal_ctrl.rotate_with_degree(rm_define.gimbal_up, randup)

                led_ctrl.set_flash(rm_define.armor_all, blink_rate[1])
                led_ctrl.set_top_led(rm_define.armor_top_all, led1, led2, led2, rm_define.effect_flash)
                led_ctrl.set_bottom_led(rm_define.armor_bottom_all, led1, led2, led2, rm_define.effect_flash)

                media_ctrl.play_sound(rm_define.media_sound_shoot, wait_for_complete_flag=True)
                media_ctrl.play_sound(rm_define.media_sound_shoot, wait_for_complete_flag=True)

                commands_exit = random.randint(1, 2)

                if commands_exit == 1:
                    continue
                elif commands_exit == 2:
                    led_ctrl.set_flash(rm_define.armor_all, blink_rate[0])
                    led_ctrl.set_top_led(rm_define.armor_top_all, led2, led1, led1, rm_define.effect_marquee)
                    led_ctrl.set_bottom_led(rm_define.armor_bottom_all, led2, led1, led1, rm_define.effect_flash)

                    gimbal_ctrl.recenter()

                    led_ctrl.set_top_led(rm_define.armor_top_all, led2, led2, led1, rm_define.effect_breath)
                    led_ctrl.set_bottom_led(rm_define.armor_bottom_all, led2, led2, 1, rm_define.effect_breath)
                    break

    # Call up the blaster_fire_example function. Be sure to properly indent the function or it won't work.

    blaster_fire_example()
