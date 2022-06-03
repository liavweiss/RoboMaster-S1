robot = robot_ctrl
gimbal = gimbal_ctrl
chassis = chassis_ctrl
media = media_ctrl
vision = vision_ctrl
armor = armor_ctrl
led = led_ctrl
define = rm_define
pid = rm_ctrl.PIDCtrl()


def start():
    # Enable manual control of chassis and gimbal.
    chassis_ctrl.enable_stick_overlay()
    gimbal_ctrl.enable_stick_overlay()
    V_avg = 1
    k = 0.65

    # Enable detection of S1 robots.
    vision_ctrl.enable_detection(rm_define.vision_detection_people)
    vision_ctrl.set_marker_detection_distance(1)

    # Fire one bead per trigger. This does not affect IR firing.
    gun_ctrl.set_fire_count(1)

    # Set gimbal rotation speed to the maximum possible, for fast object
    # tracking.
    gimbal_ctrl.set_rotate_speed(540)
    pid.set_ctrl_params(330, 0, 28)

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
        robotList = RmList(vision_ctrl.get_people_detection_info())
        print(robotList)
        if robotList[1] > 0:

            # We found at least one robot.
            robot_ctrl.set_mode(rm_define.robot_mode_chassis_follow)
            variable_x = robotList[4]
            pid.set_error(variable_x - 0.5)
            # gimbal.rotate_with_speed(pid.get_output(),0)
            v = (V_avg - (k * abs(robotList[3] / 180)))
            chassis.set_trans_speed(v * 0.5)
            chassis.move(0)

            # Cache previous x and y values.
            prevX = x
            prevY = y

            # Get coordinates to the center of the first
            # detected S1 robot. This will be our target.
            x = robotList[2]
            y = robotList[3]

            # Robot detection is currently too slow. Make sure that we do not
            # overshoot the target because we think we did not move. Note there
            # are cases this will fail miserably, but they are unlikelly.
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
                gimbal_ctrl.angle_ctrl(yawAngle + yaw, pitchAngle + pitch)

                # Fire!
                gun_ctrl.fire_once()
        else:
            # gimbal.rotate_with_speed(0,0)
            chassis_ctrl.stop()