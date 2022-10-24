""" 3d-measurements.py
After selecting pixels from an input image, this script computes the distance between each line segment, then finds the perimeter.

No esta terminado, tiene 2 modos:

El primero es para cargar una imagen guardada:
python3 3d_measurements.py --input_image chess.png --distance 1 --mode file 

El segundo activa la camara para tomar un frame y lo utiliza como imagen
python3 3d_measurements.py --input_image chess.png --distance 1 --mode live

Click izquierdo para poner puntos y crear segmentos, click derecho para conectar el punto inicial con el punto final y calcular el perimetro en pixeles

First created: Thursday 22 September, 2022

"""
#Import standard libraries
import cv2
import argparse
import numpy as np
import os

def video_cap():
    cap = cv2.VideoCapture("/dev/video1") # check this
    while(True):
        # Capture frame-by-frame
        ret, frame = cap.read()

        # Display the resulting frame
        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()