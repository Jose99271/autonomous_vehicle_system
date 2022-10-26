# SDA = pin.SDA_1
# SCL = pin.SCL_1
# SDA_1 = pin.SDA
# SCL_1 = pin.SCL

from adafruit_servokit import ServoKit
import board
import busio
import time
import signal
import numpy as np
from xbox360controller import Xbox360Controller


def _map(x, in_min, in_max, out_min, out_max):
    return int((x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)

def on_axis_moved(self, axis):
    desired_angle = (axis.x+1)/2*180
    desired_angle = _map(desired_angle,0,180,55,125)
    kit.servo[0].angle = desired_angle
    print(desired_angle)
    print('Axis {0} moved to {1} {2}'.format(axis.name, axis.x, axis.y))

        
              

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
time.sleep(0.5)

try:
    with Xbox360Controller(0, axis_threshold=0.05) as controller:
            controller.axis_l.when_moved = on_axis_moved
    
            signal.pause()
except KeyboardInterrupt:
    pass
        
            
