#################################################################################################################
#                                           RoboMaster Project                                                  #
#                                                                                                               #
#                                    Amichai Kafka & Liav weiss & Omer Michael                                  #
#################################################################################################################

# In this part of the project we will present the ability of the robot to change lighting with simple claps hand.
# 1. clap your hands two times- the robot will change his colour light.
# 2. clap your hands three times - the robot will turn off his light.


# the colour number.
l1,l2=0,255

def start():

    def red():

        led_ctrl.set_top_led(rm_define.armor_top_all,l2,l1,l1,rm_define.effect_always_on)
        led_ctrl.set_bottom_led(rm_define.armor_bottom_all,l2,l1,l1,rm_define.effect_always_on)

    def yellow():

        led_ctrl.set_top_led(rm_define.armor_top_all,l2,l2,l1,rm_define.effect_always_on)
        led_ctrl.set_bottom_led(rm_define.armor_bottom_all,l2,l2,l1,rm_define.effect_always_on)

    def blue():

        led_ctrl.set_top_led(rm_define.armor_top_all,l1,l1,l2,rm_define.effect_always_on)
        led_ctrl.set_bottom_led(rm_define.armor_bottom_all,l1,l1,l2,rm_define.effect_always_on)

    def green():

        led_ctrl.set_top_led(rm_define.armor_top_all,l1,l2,l1,rm_define.effect_always_on)
        led_ctrl.set_bottom_led(rm_define.armor_bottom_all,l1,l2,l1,rm_define.effect_always_on)

    def pink():

        led_ctrl.set_top_led(rm_define.armor_top_all,l2,l1,l2,rm_define.effect_always_on)
        led_ctrl.set_bottom_led(rm_define.armor_bottom_all,l2,l1,l2,rm_define.effect_always_on)

    def cyan():

        led_ctrl.set_top_led(rm_define.armor_top_all,l1,l2,l2,rm_define.effect_always_on)
        led_ctrl.set_bottom_led(rm_define.armor_bottom_all,l1,l2,l2,rm_define.effect_always_on)

    media_ctrl.enable_sound_recognition(rm_define.sound_detection_applause)
    led_ctrl.turn_off(rm_define.armor_all)

    while True:

        media_ctrl.cond_wait(rm_define.cond_sound_recognized_applause_twice)
        red()

        media_ctrl.cond_wait(rm_define.cond_sound_recognized_applause_twice)
        yellow()

        media_ctrl.cond_wait(rm_define.cond_sound_recognized_applause_twice)
        blue()

        media_ctrl.cond_wait(rm_define.cond_sound_recognized_applause_twice)
        green()

        media_ctrl.cond_wait(rm_define.cond_sound_recognized_applause_twice)
        pink()

        media_ctrl.cond_wait(rm_define.cond_sound_recognized_applause_twice)
        cyan()

def sound_recognized_applause_thrice(msg):
    led_ctrl.turn_off(rm_define.armor_all)