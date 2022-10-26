# Import Standard libraries
import threading
from concurrent.futures import ThreadPoolExecutor
import time
import signal
from adafruit_servokit import ServoKit
import board
import busio
import numpy as np
import cv2
from xbox360controller import Xbox360Controller

#Import user defined libraries
#import servoMultithread as servoThread
import cameraMultithread as cameraThread
import gpsMultithread as gpsThread

# creating a lock
#lock = threading.Lock()

#motores
"""def sensor1():   
#     lock.acquire()
    
    print("Initializing Servos")
    print("Initializing ServoKit")
    kit = ServoKit(channels=16)
    # kit[0] is the bottom servo
    # kit[1] is the top servo
    print("Done initializing")
    time.sleep(0.5)
    while True:
        with Xbox360Controller(0, axis_threshold=0.05) as controller:
            controller.axis_l.when_moved = servoThread.on_axis_moved
#     lock.release()"""

#camara
def sensor2():
    #lock.acquire()
    cap = cv2.VideoCapture("/dev/video2") # check this 
    while True: 
        print("camera")
        cameraThread.video_cap(cap)
    
    #lock.release()

#gps
def sensor3():
   # lock.acquire()
    while True:
        #print("gps")
        gpsThread.run_gps()
    #lock.release()

def main():
    #print("gps")
    # creating threads
    #t1 = threading.Thread(target = sensor1)
    t2 = threading.Thread(target=sensor2)
    t3 = threading.Thread(target=sensor3)

    # start threads
    #t1.start()
    t2.start()  
    t3.start()

    # wait until threads finish their job
    #t1.join()
    t2.join()
    t3.join()


if __name__ == "__main__":
    
    
    main()
    