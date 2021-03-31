# Spatial AI Webinar Apps

![realsense](https://user-images.githubusercontent.com/21957723/84605370-8a0e5300-ae51-11ea-93e9-9c1115935662.jpeg)

Spatial AI is the blending of machine learning inferencing with geometric data
from sensors, enabling robots, drones or autonomous vehicles to better
understand the world around them.

This webinar will focus on a particular sensor called a depth camera which
enables a developer to get distances to detected objects and distances between
detected objects. Depth Cameras use stereoscopic depth sensing to calculate
distances. Stereoscopic vision relies on two parallel cameras, with the sensor
calculating depth by estimating disparities between matching key-points in the
left and right images from the cameras.

![Screen Shot 2020-06-14 at 10 29 02 AM](https://user-images.githubusercontent.com/21957723/84605475-65ff4180-ae52-11ea-8767-79555c73ee0f.png)

Use cases for a depth cameras are:
1. Navigation and Mapping - Where is my robot and how do I move it around
2. Collision Avoidance - Avoid hitting objects with my robot
3. Scene Understanding - Where are the objects and how are they moving in relation to my robot and each other
4. Object Manipulation - Have a robot perform a task like grasp an object

![realsense D400 camera family](https://user-images.githubusercontent.com/21957723/84605919-2c303a00-ae56-11ea-968b-efe608c22f28.jpeg)

The alwaysAI API's support Intel's latest depth cameras from their RealSense family the D415, D435 and D435i.  All apps within this repo are built on those API’s so you will need a RealSense camera to run them.

## Apps

| Folder                     	| Description                                                                                              	|
|----------------------------	|----------------------------------------------------------------------------------------------------------	|
| realsense-basics           	| App demonstrate how to start the camera, capture and display color and depth streams from the camera 	|
| realsense-distance-between 	| App uses point cloud coordinates to get the distances between detected objects                         	|
| realsense-object-detector  	| App gets the distances from the camera to the detected objects                                        	|
| realsense-roi              	| App detects objects within a specified region of interest based on distance(s)                                            	|

## Usage
RealSense cameras require a USB 3.x connection. If you've connected to a USB
3.x connection and it still fails, try a different cable.

Use the alwaysAI CLI to build and start these apps on your development host or
edge device:

```
aai app configure
aai app install
aai app start
```

## Support

* [Docs](https://alwaysai.co/docs)
* [RealSense API](https://alwaysai.co/docs/edgeiq_api/real_sense.html)
* [Community Discord](https://discord.gg/R2uM36U)
* [Email](contact@alwaysai.co)
