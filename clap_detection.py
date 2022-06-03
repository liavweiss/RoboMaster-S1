# Make Robomaster become a cool Clap Lamp night light. Simply clap your hands twice every time to change
# his leds into your favorite colour. Clap your hands three times to turn his leds off. Type and execute/run
# the program example below and see what happens.

media=media_ctrl
led=led_ctrl
define=rm_define

l1,l2=0,255

def start():

    def red():

        led.set_top_led(define.armor_top_all,l2,l1,l1,define.effect_always_on)
        led.set_bottom_led(define.armor_bottom_all,l2,l1,l1,define.effect_always_on)

    def yellow():

        led.set_top_led(define.armor_top_all,l2,l2,l1,define.effect_always_on)
        led.set_bottom_led(define.armor_bottom_all,l2,l2,l1,define.effect_always_on)

    def blue():

        led.set_top_led(define.armor_top_all,l1,l1,l2,define.effect_always_on)
        led.set_bottom_led(define.armor_bottom_all,l1,l1,l2,define.effect_always_on)

    def green():

        led.set_top_led(define.armor_top_all,l1,l2,l1,define.effect_always_on)
        led.set_bottom_led(define.armor_bottom_all,l1,l2,l1,define.effect_always_on)

    def pink():

        led.set_top_led(define.armor_top_all,l2,l1,l2,define.effect_always_on)
        led.set_bottom_led(define.armor_bottom_all,l2,l1,l2,define.effect_always_on)

    def cyan():

        led.set_top_led(define.armor_top_all,l1,l2,l2,define.effect_always_on)
        led.set_bottom_led(define.armor_bottom_all,l1,l2,l2,define.effect_always_on)

    media.enable_sound_recognition(rm_define.sound_detection_applause)
    led.turn_off(define.armor_all)

    while True:

        media.cond_wait(define.cond_sound_recognized_applause_twice)
        red()

        media.cond_wait(define.cond_sound_recognized_applause_twice)
        yellow()

        media.cond_wait(define.cond_sound_recognized_applause_twice)
        blue()

        media.cond_wait(define.cond_sound_recognized_applause_twice)
        green()

        media.cond_wait(define.cond_sound_recognized_applause_twice)
        pink()

        media.cond_wait(define.cond_sound_recognized_applause_twice)
        cyan()

def sound_recognized_applause_thrice(msg):
    led.turn_off(define.armor_all)