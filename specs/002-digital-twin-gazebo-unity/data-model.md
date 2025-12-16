# Data Model: Module 2: The Digital Twin (Gazebo & Unity)

This document defines the key entities relevant to the concepts discussed in this module. These are primarily conceptual entities for understanding, not data structures for implementation.

## Digital Twin

A virtual representation of a physical system, designed to mirror its real-world counterpart.

**Attributes**:
-   `fidelity`: Level of detail and accuracy (e.g., physics, visual, sensor).
-   `purpose`: The primary use case (e.g., simulation, testing, monitoring).

## Gazebo

A powerful open-source 3D robotics simulator, known for its robust physics engine.

**Attributes**:
-   `physics_engine`: The underlying physics simulation software (e.g., ODE, Bullet).
-   `robot_model`: Description of the robot (e.g., URDF).
-   `environment`: Description of the simulated world (e.g., SDF).

## Unity

A popular real-time 3D development platform capable of creating high-fidelity visualizations and interactive simulations.

**Attributes**:
-   `rendering_pipeline`: Method for visual output (e.g., HDRP, URP).
-   `asset_pipeline`: How 3D models and textures are managed.
-   `interaction_mechanisms`: How users or other systems interact with the simulation.

## LiDAR

A remote sensing method that uses light in the form of a pulsed laser to measure ranges.

**Attributes**:
-   `range`: Maximum detection distance.
-   `angular_resolution`: Density of measurements.
-   `noise_model`: Characteristics of simulated errors.

## Depth Camera

A camera that produces an image where each pixel's value corresponds to the distance from the camera to the object.

**Attributes**:
-   `resolution`: Image dimensions (width x height).
-   `field_of_view`: Angular extent of the scene captured.
-   `noise_model`: Characteristics of simulated errors.

## IMU (Inertial Measurement Unit)

An electronic device that measures and reports a body's specific force, angular rate, and sometimes the magnetic field surrounding the body.

**Attributes**:
-   `acceleration_axes`: Number of accelerometer axes.
-   `gyroscope_axes`: Number of gyroscope axes.
-   `noise_model`: Characteristics of simulated errors (e.g., drift, bias).

## Physics Engine

A computer program that simulates physical models, typically a part of a larger simulation environment.

**Attributes**:
-   `accuracy`: Precision of calculations.
-   `performance`: Computational speed.
-   `features`: Specific physical phenomena simulated (e.g., fluid dynamics, soft bodies).
