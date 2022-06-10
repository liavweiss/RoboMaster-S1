# RoboMaster-S1
### Final project in Autonomous Robots Course.
![RoboMaster](https://github.com/liavweiss/RoboMaster-S1/blob/main/docs/RoboMaster.PNG)


#### Introduction:
In this project we present different abilities of the robot to perform autonomous tasks.  
The robot abilities:
* Change light with simple claps hand.
* Follow after line.
* Follow and shot a person.
* Follow and shot a robot.
---------------------------------------------------
#### Change light with simple claps hand:
In this part of the project we will present the ability of the robot to change lighting with simple claps hand.
1. clap your hands two times- the robot will change his colour light.
2. clap your hands three times - the robot will turn off his light.

---------------------------------------------------
#### Follow after line:
In this part of the project we will present the ability of the robot to follow a line.
In this code the robot will follow a red line, but you can easily change the color
of the line that the robot is following using line_follow_color_<color> located on line 30.
First we lower the gimbal to look at the floor and after that as soon as the robot detects the red line it will move towards it, we have chosen the speed of the robot to be slower so that the robot can make sharp turns.

---------------------------------------------------
#### Follow and shot a person:
In this part of the project we will present the robot's ability to track and shoot a person.
First we want to control the chassis the and gimbal manual, after that we will Enable detection of persons.
We will set the gimbal rotation speed to the maximum possible, for fast object.
We will set the travel mode to free mode so we can automatically rotate the gimbal.
To truck after the persom we will need to save his previous possitions and his current position.
After that as long as we recognize the human we will track his location and shoot at him non-stop,
as soon as the person comes out of the robot's mediator of vision the robot will stop and wait (to use as little battery of the robot as possible).
  
  ---------------------------------------------------
#### Follow and shot a robot:
In this part of the project we will present the robot's ability to track and shoot a robot.
First we want to control the chassis the and gimbal manual, after that we will Enable detection of robot.
We will set the gimbal rotation speed to the maximum possible, for fast object.
We will set the travel mode to free mode so we can automatically rotate the gimbal.
To truck after the robot we will need to save his previous possitions and his current position.
After that as long as we recognize the robot we will track his location and shoot at him non-stop,
as soon as the robot comes out of the robot's mediator of vision the robot will stop and wait (to use as little battery of the robot as possible).








<!-- CONTACT -->
## Contact

* Liav Weiss - [@liavweiss](https://github.com/liavweiss) - liavweiss@gmail.com
* Amichai Kafka - [@amichaikafka](https://github.com/amichaikafka) - amichaikp@gmail.com
* Omer Michael - [@omerMichael](https://github.com/omerMichael) - Omerikop2145@gmail.com

<!-- EXTERNAL DOCSS -->
## External docs
* [RoboMaster](https://en.wikipedia.org/wiki/RoboMaster) - More about RoboMaster.

