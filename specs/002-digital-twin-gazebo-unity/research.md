# Research: Module 2: The Digital Twin (Gazebo & Unity)

This document records the research and decisions made for the "Digital Twin" module.

## Gazebo vs. Unity for Robotics Simulation

**Decision**: The module will explain both Gazebo and Unity, highlighting their distinct strengths and weaknesses for robotics simulation. Gazebo will be presented for physics-accurate simulation, and Unity for high-fidelity visualization and human-robot interaction.

**Rationale**: The module's focus is on digital twins, which often leverage different tools for different aspects (e.g., physics vs. rendering). Understanding both platforms provides a comprehensive view. The spec explicitly states "Reader can explain differences between Gazebo and Unity".

**Alternatives considered**:
- Focusing solely on Gazebo: Would miss the high-fidelity visualization aspects important for digital twins.
- Focusing solely on Unity: Would undersell the robust physics simulation capabilities of Gazebo.

## Sensor Simulation Realism

**Decision**: The module will cover the conceptual aspects of simulating various sensors (LiDAR, depth cameras, IMUs) and emphasize the importance of noise models and realism constraints.

**Rationale**: Realistic sensor data is crucial for developing robust perception pipelines. Understanding the limitations and modeling of noise is essential for students. The spec includes "Reader can reason about simulated sensor data limitations".

**Alternatives considered**:
- Skipping sensor simulation: Would leave a critical gap in understanding digital twins for perception.
- Deep dive into specific sensor models: Too detailed for a conceptual module; focus is on broad understanding.

## Scope of "Not Building" Items

**Decision**: Explicitly reiterate the "Not Building" items from the feature description to manage expectations. This includes avoiding game development tutorials, full sensor calibration pipelines, hardware-specific simulation tuning, and real-world deployment guides.

**Rationale**: Maintaining a clear scope ensures the module remains focused on core digital twin concepts and avoids overwhelming the target audience with tangential topics.

**Alternatives considered**:
- Including some "Not Building" items: Would expand the scope unnecessarily and deviate from the core focus.
