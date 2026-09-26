# Robot Simulation

ROS 2 Jazzy + Gazebo Harmonic robot simulation.

## Environment

- Ubuntu 24.04 LTS
- ROS 2 Jazzy
- Gazebo Harmonic
- RViz2
- WSL2

## Project

A simulated robot model developed using ROS 2 and Gazebo.
## Dynamic Obstacle Demonstration

The competition world contains a dynamic obstacle that moves continuously
between x = -4 m and x = 4 m along y = 4 m.

### Start the simulation

Build the workspace:

```bash
cd ~/robot-simulation
colcon build
source install/setup.bash
