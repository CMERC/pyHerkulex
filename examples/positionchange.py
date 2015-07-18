import herkulex
from herkulex import servo
herkulex.connect("/dev/tty.usbserial", 115200)
servoid = 13
s = servo()
s.torque_on()                 
s.set_servo_position(100,100,0x08)
