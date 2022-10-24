# SDA = pin.SDA_1
# SCL = pin.SCL_1
# SDA_1 = pin.SDA
# SCL_1 = pin.SCL

from adafruit_servokit import ServoKit
import board
import busio
import time


# On the Jetson Nano
# Bus 0 (pins 28,27) is board SCL_1, SDA_1 in the jetson board definition file
# Bus 1 (pins 5, 3) is board SCL, SDA in the jetson definition file
# Default is to Bus 1; We are using Bus 0, so we need to construct the busio first ...
print("Initializing Servos")
print("Initializing ServoKit")
kit = ServoKit(channels=16)
# kit[0] is the bottom servo
# kit[1] is the top servo
print("Done initializing")
# sweep = range(0,180)
# for degree in sweep :
while True:
    kit.servo[0].angle = 125
    time.sleep(0.5)
    kit.servo[0].angle = 55
    time.sleep(0.5)
#     # kit.servo[1].angle=degree
#     # time.sleep(0.01)

# time.sleep(0.5)
# sweep = range(180,0, -1)
# for degree in sweep :
#     kit.servo[0].angle=degree
    
# last_presses = None
# while True:
#        with ControllerResource() as joystick:
#            print(type(joystick).__name__)
#            while joystick.connected:
#                 axis_list = [ 'lx', 'ry' ]
#                 for axis_name in axis_list:
#                     # desired_angle is in degrees
#                     joystick_value = joystick[axis_name]
#                     # The joystick value goes from -1.0 ... 1.0 (a range of 2)
#                     # Normalize within a range of 180 degrees
#                     desired_angle = (joystick_value+1)/2*180
                    
#                     if  axis_name == 'lx' :
#                         kit.servo[0].angle=desired_angle
#                         # print(axis_name, joystick[axis_name])
                        
#                     if axis_name == 'ry' :
#                          kit.continuous_servo[1].throttle=joystick[axis_name]