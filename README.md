# Lane Following with Carla

This repository contains a Python script for implementing a basic lane-following algorithm using the Carla simulator. The script utilizes the Carla Python API to connect to the simulator, spawn a Tesla Model 3 vehicle, and attach a camera sensor to the vehicle. The camera sensor captures images, and the script processes these images to detect lanes and control the vehicle accordingly.

## Dependencies
- [Carla Simulator](https://carla.org/): Make sure to have Carla installed and running on your system.
- Python 3.x
- OpenCV
- NumPy

## Setup

1. **Install Dependencies**: Ensure that you have Carla installed on your machine, and install the required Python libraries using:

    ```bash
    pip install numpy opencv-python
    ```

2. **Run Carla Server**: Start the Carla server on your machine.

3. **Adjust Configuration**: Modify the script to match your Carla server configuration and adjust parameters if needed.

## Usage

1. **Run the Script**: Execute the script to connect to the Carla server, spawn the vehicle, and begin the lane-following algorithm.

    ```bash
    python lane_following.py
    ```

2. **Simulation**: Observe the lane detection and steering logic in the Carla simulator as the vehicle navigates the environment.

3. **Exit the Script**: Press `Ctrl + C` to stop the script and clean up resources.

## Lane Following Algorithm

The `lane_following` function processes camera images to perform lane detection using color segmentation, edge detection, and Hough Transform. The steering angle is then calculated based on the average position of the detected lanes. The script continuously runs the algorithm, providing real-time lane-following behavior.

Feel free to modify and enhance the script to suit your needs or integrate more advanced algorithms for autonomous driving.

## Notes

- This script is a basic example for educational purposes and may require adjustments for different Carla environments or scenarios.
- Make sure to comply with Carla's usage terms and conditions when using the simulator for research or development.

Drive safely, Follow the lanes! 🚗🛣️
