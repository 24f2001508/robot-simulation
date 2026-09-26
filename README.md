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

## Dual-Path A-to-B Topology

The competition arena provides two distinct routes between the start
and goal regions:

### Route 1 — Direct Incline Route

A direct route toward the goal uses the elevated platform/ramp.
This route introduces three-dimensional displacement and elevation.

### Route 2 — Zig-Zag Ground Route

A second route remains on the ground plane at z = 0 and uses the
zig-zag obstacle corridor. This route provides a longer 2D travel
path while avoiding the elevated section.

The two routes are intended to provide different terrain and distance
trade-offs for global path planning.
