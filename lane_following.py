import carla
import numpy as np
import cv2

#connect to the carla server 
client = carla.Client('localhost', 2000)
client.set_timeout(10.0)