# ​🚥🤖​Smart Traffic Lights​🚥🤖​
Hello World ​👾

This repository is a smart traffic lights project, maded with python3, openCV and pre-trained Haar Clasifier for car detection.

## How Works
This software takes advantage of vehicle density calculated with image processing using OpenCV and one pre-trained Haar Classifier model, to optimize the time of the signals of the traffic lights. And Giving remote control over the traffic light for emergencies.

### Components

<ul>
<li>Raspberry Pi 3 Model B</li>
<li>Arduino Nano</li>
<li>Pre-trained Haar Clasifier Model</li>
<li>OpenCV</li>
</ul>

An Raspberry Pi 3 Model B is used for image processing. The basic approach is that the raspberry will take into account the vehicle density in a time interval, taking into account the current time, this vehicle density will be called "Car Ratio". Once the value is obtained, the software will be in charge of calculating the amount of time needed for each traffic light, then, through the I2C interface, it is proposed to report this value to the slave controllers (Arduino nanos) which are in charge of the cycles of each traffic light. .
