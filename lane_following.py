import carla
import numpy as np
import cv2

#connect to the carla server 
client = carla.Client('localhost', 2000)
client.set_timeout(10.0)

#access the world and blueprint library

world = client.get_world()
blueprint_library = world.get_blueprint_library()

#spawn a vehicle 

#Choose a vehicle blueprint
vehicle_bp = blueprint_library.find('vehicle.tesla.model3')

#choose a spawn point
spawn_point = world.get._map.get_spawn_points()[0]

#spawn the vehicle
vehicle = world.spawn_actor(vehicle_bp, spawn_point)

#create a camera sensor and attach it to the vehicle

camera_bp = blueprint_library.find('sensor.camera.rgb')
camera_transform = carla.Transform(carla.Location(x=1.5, z=2.4))
camera = world.spawn_actor(camera_bp, camera_transform, attach_to = vehicle)