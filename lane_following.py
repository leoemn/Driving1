import carla
import numpy as np
import cv2
import time

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
spawn_point = world.get_map().get_spawn_points()[0]

#spawn the vehicle
vehicle = world.spawn_actor(vehicle_bp, spawn_point)

#create a camera sensor and attach it to the vehicle

camera_bp = blueprint_library.find('sensor.camera.rgb')
camera_transform = carla.Transform(carla.Location(x=1.5, z=2.4))
camera = world.spawn_actor(camera_bp, camera_transform, attach_to = vehicle)

# Constants
CAMERA_HEIGHT = 480
CAMERA_WIDTH = 640

# Parameters for lane detection
lower_yellow = np.array([18, 80, 80])
upper_yellow = np.array([30, 255, 255])

# Function to process the camera image and control the vehicle
def lane_following(image):
    # Convert the image to OpenCV format (BGR)
    img = np.array(image.raw_data).reshape((CAMERA_HEIGHT, CAMERA_WIDTH, 4))[:, :, :3]

    # Convert BGR to HSV
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # Create a mask for yellow color
    yellow_mask = cv2.inRange(hsv, lower_yellow, upper_yellow)

    # Combine the original image with the yellow mask
    result = cv2.bitwise_and(img, img, mask=yellow_mask)

    # Convert the result to grayscale
    gray = cv2.cvtColor(result, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian blur to reduce noise and help with edge detection
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # Use Canny edge detection to find edges in the image
    edges = cv2.Canny(blurred, 50, 150)

    # Find lines using Hough Transform
    lines = cv2.HoughLinesP(edges, 1, np.pi / 180, threshold=50, minLineLength=100, maxLineGap=50)

    # Draw the detected lines on the original image
    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line[0]
            cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 3)

    # Display the resulting image
    cv2.imshow("Lane Detection", img)
    cv2.waitKey(1)

    # Basic steering logic: steer towards the average position of detected lanes
    steering_angle = 0.0
    if lines is not None:
        lane_positions = [(x1 + x2) / 2 for line in lines for x1, _, x2, _ in line]
        if lane_positions:
            avg_lane_position = sum(lane_positions) / len(lane_positions)
            steering_angle = (avg_lane_position - CAMERA_WIDTH / 2) / (CAMERA_WIDTH / 2)

    # Example: Restrict the steering angle for smoother control
    steering_angle = max(min(steering_angle, 1.0), -1.0)

    # Print the steering angle (for testing)
    print(f"Steering Angle: {steering_angle}")

    # Return the steering angle to control the vehicle
    return steering_angle

# Set up a callback function for the camera
camera.listen(lambda image: lane_following(image))

try:
    while True:
        # Run your lane-following algorithm continuously
        world.tick()
        time.sleep(0.1)  # Add a delay (in seconds) to control the frequency

finally:
    # Clean up
    cv2.destroyAllWindows()
    camera.destroy()
    vehicle.destroy()
