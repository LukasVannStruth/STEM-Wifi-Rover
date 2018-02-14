# STEM-Wifi-Rover
This repository contains the scripts that are used when remoting into our rover. 

# Installation
### Requirements:
In order to install and run the two programs contained within this repository you must have python 3.6 installed as well the the Arduino IDE. 
### Arduino Sketch Installation
To run the Arduino code simply open the Tethered-Rover/Tethered-Rover.ino file in the Arduino IDE and upload it to your Arduino setup. 
You must download the Adafruit Motor Shield Library v1 firmware in either the Arduino IDE Library manager or downloading it manually at https://github.com/adafruit/Adafruit-Motor-Shield-library
Instructions for how to configure the sketch to your individual rover configuration arecontained within the Arduino Sketch itself. 
### Python Client installation
In order to use the Python client to control the rover you must first have Python 3 installed on your computer. I have only tested this on Python 3.6, but other version may work. Once Python itself is installed, run these commands from a terminal(should work on Windows, but I haven't confirmed):
>cd $PROJECT_ROOT/keyboardinput
>
>pip install .

Running these commands should install both the module itself as well as the libraries needed for the client to function. Once pip finishes it's task, all you should need to do is run the command 'keyboardinput' in a terminal and the process will run correctly. Default Rover Control keybindings:
> W/Up Arrow: All motors accelerate forward
>
> A/Left Arrow: Right motors go forward, left motors go back so the rover spins in a counter-clockwise direction.
>
> S/Down Arrow: All motors go backwards.(This does not stop the rover, use F for that.)
>
> D/Right Arrow: Left motors go forward and right motors go back, spinning the rover in a clockwise direction. 
>
> F: Stops all of the motors. 