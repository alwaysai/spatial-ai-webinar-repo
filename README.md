# spatial-ai-webinar-repo
![realsense](https://user-images.githubusercontent.com/21957723/84605370-8a0e5300-ae51-11ea-93e9-9c1115935662.jpeg)

Spatial AI is the blending of machine learning inferencing with geometric data from sensors, enabling  robots, drones or autonomous vehicles to better understand the world around them in which they operate.

This webinar will focus on particular sensor called a depth camera which enables a developer in their programs to get distances to detected objects and distances between detected objects.  Depth Cameras use stereoscopic depth sensing to calculate distances.  Stereoscopic vision relies on two parallel cameras and the sensor calculates depth by estimating disparities between matching key-points in the left and right images from the cameras.
![Screen Shot 2020-06-14 at 10 29 02 AM](https://user-images.githubusercontent.com/21957723/84605475-65ff4180-ae52-11ea-8767-79555c73ee0f.png)

Use cases for a depth cameras are:
1. Navigation and Mapping - Where is my robot and how do I move it around
2. Collision Avoidance - Avoid hitting objects with my robot
3. Scene Understanding - Where are the objects and how are they moving in relation to my robot and each other
4. Object Manipulation - Have a robot perform a task like grasp an object
![realsesne D400 camera famliy](https://user-images.githubusercontent.com/21957723/84605919-2c303a00-ae56-11ea-968b-efe608c22f28.jpeg)

The alwaysAI API’s support Intel’s latest depth cameras from their Realsense family the D415, D435 and D435i.  All apps within this repo are built on those API’s so you will need a Realsense camera to run them.

## Repo Programs
| Folder                     	| Description                                                                                              	|
|----------------------------	|----------------------------------------------------------------------------------------------------------	|
| realsenes-basics           	| Program demonstrate how to start the camera, capture and display color and depth streams from the camera 	|
| realsense-distance-between 	| Program uses point cloud coordinates to get the distances between detected objects                         	|
| realsense-object-detector  	| Program gets the distances from the camera to the detected objects                                        	|
| realsense-roi              	| Program detects objects within a specified region of interest based on distance(s)                                            	|
| object-detector            	| Standard alwaysAI object detector                                                                        	|
## Running
Use the alwaysAI CLI to build and start these apps on Linux PCs and Devices:

Configure (once): `aai app configure`

Build: `aai app deploy`

Run: `aai app start`

If you are using a Mac or Windows 10 PC do the following:

Configure (once): `aai app configure`

Build: `aai app install`

Run: `aai app start`


## Support
Docs: https://dashboard.alwaysai.co/docs/getting_started/introduction.html

Realsense API Docs: https://alwaysai.co/docs/edgeiq_api/real_sense.html

Community Discord: https://discord.gg/R2uM36U

Email: contact@alwaysai.co
