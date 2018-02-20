#imports the curses library

import curses

#imports the motor shield library

from pololu_drv8835_rpi import motors, MAX_SPEED

#these are the default values for the motor speeds
speed = MAX_SPEED

reversespeed = speed * -1
#Functions
#The parameters for speed are in percent (eg. go_forward(0.7) would go forward at 70% speed; 
#default is 100%)

def stop():
    motors.setSpeeds(0, 0)

def go_forward():
    motors.setSpeeds(speed, speed)

def go_backward():
    motors.setSpeeds(reversespeed, reversespeed)

def turn_left():
    motors.setSpeeds(speed, reversespeed)

def turn_right():
    motors.setSpeeds(reversespeed, speed)

def main():
    #set up curses window
    STDSCR = curses.initscr()
    #turn off keys echoing to screen
    #react to keys being pressed instantaneously instead of   waiting for enter to be pressed
    curses.cbreak()
    #replace default values returned with things like the  arrow keys to things like curses.KEY_LEFT
    STDSCR.keypad(True)

    STDSCR.addstr("To exit the program, press CTRL + C in order to quit the process. ")
    #To change keybindings for the movement change 
    #the keys shown here. You may need to refer to the 
    #python curses documentation which can be reached at    https://docs.python.org/3/library/curses.html for  non-ascii keys. 
    while True: 
        input_char = STDSCR.getch()
        STDSCR.addstr(input_char)
        if input_char == ord('w') or input_char == curses.KEY_UP:   
            go_forward()
            stop()
        elif input_char == ord('s') or input_char == curses.KEY_DOWN:
            go_backward()
            stop()
        elif input_char == ord('a') or input_char == curses.KEY_LEFT:
            turn_left()
            stop()    
        elif input_char == ord('d') or input_char == curses.KEY_RIGHT:
            turn_right()
            stop()
        elif input_char == ord('f'):
            stop()
        STDSCR.
try:      
    main()
finally:    
    stop()