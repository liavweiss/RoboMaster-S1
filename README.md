# RoboMaster-S1
### Final project in Autonomous Robots Course.
![RoboMaster](https://github.com/liavweiss/RoboMaster-S1/blob/main/docs/RoboMaster.PNG)


### Introduction:
In this project we present different abilities of the robot to perform autonomous tasks.  

### RoboMaster-S1 Coordinate system:
* ![Coordinate system1](https://github.com/liavweiss/RoboMaster-S1/blob/main/docs/Coordinate system1.jpg)
* ![RoboMaster](https://github.com/liavweiss/RoboMaster-S1/blob/main/docs/Coordinate system2.jpg)

--------------------------------------------------
### Robot abilities:
* Change light with simple claps hand.
* Shot a person.
* Follow after line.
* Follow and shot a person.
* Follow and shot a robot.
* Detect and shot a marker
---------------------------------------------------
#### Change light with simple claps hand:
In this part of the project we will present the ability of the robot to change lighting with simple claps hand.
1. clap your hands two times- the robot will change his colour light.
2. clap your hands three times - the robot will turn off his light.

Video showing the 'Change light with simple claps hand' abillity: https://youtube.com/shorts/pCJINt0g5TY?feature=share

---------------------------------------------------
#### Shot a person:
In this part of the project we will present the robot's ability to fire his blaster every time he sees a person.
Set the vision marker detection distance from 0.5 to 3 for farther distances.

---------------------------------------------------
#### Follow after line:
In this part of the project we will present the ability of the robot to follow a line.
In this code the robot will follow a red line, but you can easily change the color
of the line that the robot is following using line_follow_color_<color> located on line 30.
First we lower the gimbal to look at the floor and after that as soon as the robot detects the red line it will move towards it, we have chosen the speed of the robot to be slower so that the robot can make sharp turns. 

Video showing the 'Follow after line' abillity: https://youtube.com/shorts/tX8VVClE-zo?feature=share
  
---------------------------------------------------
#### Follow and shot a person:
In this part of the project we will present the robot's ability to track and shoot a person.
First we want to control the chassis the and gimbal manual, after that we will Enable detection of persons.
We will set the gimbal rotation speed to the maximum possible, for fast object.
We will set the travel mode to free mode so we can automatically rotate the gimbal.
To truck after the persom we will need to save his previous possitions and his current position.
After that as long as we recognize the human we will track his location and shoot at him non-stop,
as soon as the person comes out of the robot's mediator of vision the robot will stop and wait (to use as little battery of the robot as possible).
  
Video showing the 'Follow and shot a person' abillity: https://youtube.com/shorts/ZHSRRkfaaq0?feature=share
  
---------------------------------------------------
#### Follow and shot a robot:
In this part of the project we will present the robot's ability to track and shoot a robot.
First we want to control the chassis the and gimbal manual, after that we will Enable detection of robot.
We will set the gimbal rotation speed to the maximum possible, for fast object.
We will set the travel mode to free mode so we can automatically rotate the gimbal.
To truck after the robot we will need to save his previous possitions and his current position.
After that as long as we recognize the robot we will track his location and shoot at him non-stop,
as soon as the robot comes out of the robot's mediator of vision the robot will stop and wait (to use as little battery of the robot as possible).

Video showing the 'Follow and shot a robot' abillity: https://youtube.com/shorts/uaK8NHYSVts

  
---------------------------------------------------
#### Detect and shot a marker:
In this part of the project we will present the ability of the robot to search for a mark follow and shot him.
First we want to rotate the gimbal to see if we recognize any marker,
as soon as we see a certain marker we will save it and rotate the gimbal again until we recognize the same marker,
as soon as we recognize the same marker we will make a slow move to it and shoot at it.
It is important to note that if we see on the way another marker we will ignore it.

Video showing the 'Follow and shot a marker' abillity: https://youtube.com/shorts/ZrU5j08cnVE?feature=share

--------------------------------------------------------
### our experiment:
There are other abilities in the project (see in our GitHub) but in this report we tested the following abilities:
  1.	Follow and shot person.
    a.	Link to the experiment video: https://youtube.com/shorts/wKOpfwJcW9Q?feature=share
  2.	Follow and shot robot.
    a.	Link to the experiment video: https://youtube.com/shorts/A__nEGU-DuU?feature=share
  3.	Follow and shot marker.
    a.	Link to the experiment video: https://youtube.com/shorts/FXZyLtb0pik

In this report we will present two important parameters in each component:
  1.	The time it took for the robot to identify the object
  2.	The time it took for the robot to reach it.
  
  | **Tasks**      |    **Detection time:**        |           Arrival Time:                  |
|-----------------|-----------------------|---------------------------------------------------|
| Follow and shot person: | 00:02.84 seconds |                00:09.85 seconds         |
| Follow and shot robot: | 00:03.21 seconds |                 00:10.19 seconds    |
| Follow and shot marker: | 00:05.20 seconds |                00:10.03 seconds               |

It can be seen from the process that the robot took longer to identify the symbols than to identify the person figure or the robot figure, it can cause because the symbols is much smaller and it is harder to spot it outside. We can say that the robot knows how to deal with terrain conditions (such as sunlight and darkness) but this can affect the detection times of the robot.
  
----------------------------------------------------------
### Similar projects:
  
https://www.youtube.com/watch?v=e1j9YqC2YfI&ab_channel=JaffeLing  
https://www.youtube.com/watch?v=L-c5KgZZA_0&ab_channel=Science%26Imagination
  
----------------------------------------------------------  
  
<!-- CONTACT -->
### Contact

* Liav Weiss - [@liavweiss](https://github.com/liavweiss) - liavweiss@gmail.com
* Amichai Kafka - [@amichaikafka](https://github.com/amichaikafka) - amichaikp@gmail.com
* Omer Michael - [@omerMichael](https://github.com/omerMichael) - Omerikop2145@gmail.com
  
-----------------------------------------------
  
<!-- EXTERNAL DOCSS -->
### External docs
* [RoboMaster](https://en.wikipedia.org/wiki/RoboMaster) - More about RoboMaster.

