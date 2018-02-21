#######################################################
########  Arduino I/O Slave Control  ##################
#######################################################

############### Import needed libraries ###############
from Tkinter import *
from time import sleep
from webserver import WebServer
import serial, atexit
############### Communication SETUP ###############
arduino_port = '/dev/serial0' #     usbport = '/dev/ttyUSB0' = 'COM3' = '/dev/tty.usbserial-FTALLOK2'

try:
    ser = serial.Serial(arduino_port, 9600, timeout=1)
except:
    print"serial ain't workin boss..."

def updatePWM(portObject, pwmDC):  ## Format the data into a 3 Byte packet
##  the chr() function converts a value between 0-255 into a 
    ser.write(chr(255))  ## (1st Byte) this is the start byte
##    print(chr(255))
    ser.write(chr(portObject))  ## (2nd byte) this is object number
##    print(chr(portObject))
    ser.write(chr(pwmDC))  ##(3rd byte) this is the PWM duty cycle
##    print(chr(pwmDC))
    print("Serial Commands:", (chr(255), chr(portObject), chr(pwmDC)))
    print("Serial Commands:", (255, portObject, pwmDC))

def init():
    updatePWM(1, 90) ## Victor ESC 1 (pin 9)
    updatePWM(2, 90) ## Victor ESC 2 (pin10)
    updatePWM(3, 90) ## Servo 1 (pin11)

############### Update Arduino PWM ###############

def slider1_val(slid1):
    updatePWM(1, int(slid1)) ## Parse it into an integer
##    print(int(slid1), slid1)

def slider2_val(slid2):
    updatePWM(2, int(slid2)) ## Parse it into an integer
##    print(int(slid2), slid2)

############### GUI SETUP ###############

root = Tk()  ## Create a window object named "root"

topFrame = Frame(root)  ## Create a invisible partition frame named "topFrame"
topFrame.pack(side=TOP)  ## Place that partition in the top of the window
bottomFrame = Frame(root)  ## Create a invisible partition frame named "bottomFrame"
bottomFrame.pack(side=BOTTOM)  ## Place that partition in the bottom of the window

theLabel = Label(topFrame, text="Motor Controller")  ## Create a label and place it in the Window named root
theLabel.pack()  ## Place the "theLabel" into the first available space

slider1 = Scale(topFrame, length=200, command=slider1_val, from_=0, to=180, orient=VERTICAL, label="Left")  ## Create a scale object and setup
slider2 = Scale(topFrame, length=200, command=slider2_val, from_=0, to=180, orient=VERTICAL, label="Right")
button3 = Button(bottomFrame, text="LED ON/OFF", fg="Blue")  ## Create a button object and place it into a frame and have text inside and color it

slider1.pack(side=LEFT, fill=Y)
slider2.pack(side=RIGHT)

theLabel = Label(bottomFrame, text="Routine", fg="Blue")  ## Create a label and place it in the Window named root
theLabel.pack()  ## Place the "theLabel" into the first available space

button3.pack()

root.mainloop()  ## Run cont. until somebody hits the exit button
    
init()
updatePWM()

def exit_handler():
    updatePWM(1, 90) ## Victor ESC 1 (pin 9)
    updatePWM(2, 90) ## Victor ESC 2 (pin10)

atexit.register(exit_handler)
