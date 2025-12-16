# Data Model for Module 4: Vision-Language-Action (VLA)

This document outlines the key entities involved in the Vision-Language-Action (VLA) module, focusing on their conceptual attributes and relationships.

## Entities

### 1. Voice Command
*   **Description**: The natural language audio input provided by the user.
*   **Attributes**:
    *   `audio_data`: Raw audio stream or file.
    *   `timestamp`: Time of command issuance.
    *   `user_id`: (Optional) Identifier for the user.
*   **Relationships**: Transcribed Text (produces)

### 2. Transcribed Text
*   **Description**: The text representation of the voice command, output by OpenAI Whisper.
*   **Attributes**:
    *   `text_content`: String of the transcribed command.
    *   `language`: Detected language of the transcription.
    *   `confidence`: (Optional) A confidence score for the transcription.
*   **Relationships**: Voice Command (derived from), LLM Model (input to)

### 3. LLM Model
*   **Description**: The Large Language Model responsible for interpreting transcribed text and generating cognitive plans. This is a conceptual entity representing the AI component.
*   **Attributes**:
    *   `model_name`: Identifier of the LLM used (e.g., GPT-4, Llama 2).
    *   `version`: Version of the model.
    *   `parameters`: Key configuration parameters (e.g., temperature, max_tokens).
*   **Relationships**: Transcribed Text (consumes), Cognitive Plan (produces)

### 4. Cognitive Plan
*   **Description**: The high-level plan derived from the LLM, detailing a sequence of abstract steps to achieve the user's goal.
*   **Attributes**:
    *   `plan_id`: Unique identifier for the plan.
    *   `goal_description`: Natural language description of the overall goal.
    *   `abstract_steps`: Ordered list of high-level actions (e.g., "Go to kitchen", "Pick up cup").
    *   `status`: (e.g., "pending", "in_progress", "completed", "failed").
*   **Relationships**: LLM Model (derived from), ROS 2 Action Sequence (translated into)

### 5. ROS 2 Action Sequence
*   **Description**: The detailed, executable series of ROS 2 commands (topics, services, actions) translated from the cognitive plan, driving specific robot behaviors.
*   **Attributes**:
    *   `sequence_id`: Unique identifier for the action sequence.
    *   `actions`: Ordered list of ROS 2 primitives (e.g., `navigate_to_pose`, `pick_object`).
    *   `parameters`: Parameters for each ROS 2 action (e.g., `x, y, yaw` for navigation; `object_id` for picking).
    *   `status`: (e.g., "executing", "paused", "completed", "error").
*   **Relationships**: Cognitive Plan (derived from), Simulated Robot (executed by)

### 6. Simulated Robot
*   **Description**: The virtual autonomous humanoid, including its sensors (e.g., camera, lidar) and effectors (e.g., wheels, manipulators).
*   **Attributes**:
    *   `robot_id`: Unique identifier for the robot.
    *   `current_pose`: (x, y, z, roll, pitch, yaw) in the environment.
    *   `sensor_data`: Current readings from camera, lidar, joint encoders.
    *   `effector_state`: State of manipulators, grippers.
    *   `battery_level`: Current battery status.
*   **Relationships**: Simulated Environment (operates within), ROS 2 Action Sequence (executes), Target Object (interacts with), Obstacle (avoids)

### 7. Simulated Environment
*   **Description**: The virtual world where the robot operates, containing objects, obstacles, and defined areas.
*   **Attributes**:
    *   `environment_id`: Unique identifier.
    *   `map_data`: 2D/3D map of the environment.
    *   `object_locations`: Current poses of all static and dynamic objects.
    *   `lighting_conditions`: (Optional) Environmental rendering parameters.
*   **Relationships**: Simulated Robot (contains), Target Object (contains), Obstacle (contains)

### 8. Target Object
*   **Description**: A specific object within the simulated environment that the robot is instructed to identify and manipulate.
*   **Attributes**:
    *   `object_id`: Unique identifier.
    *   `object_type`: (e.g., "cup", "book", "block").
    *   `current_pose`: (x, y, z, roll, pitch, yaw) in the environment.
    *   `dimensions`: (length, width, height).
    *   `grasp_points`: (Optional) Predefined points for manipulation.
*   **Relationships**: Simulated Environment (contained in), Simulated Robot (interacts with)

### 9. Obstacle
*   **Description**: Any element in the simulated environment that impedes the robot's direct path and needs to be avoided.
*   **Attributes**:
    *   `obstacle_id`: Unique identifier.
    *   `obstacle_type`: (e.g., "box", "wall", "dynamic_person").
    *   `current_pose`: (x, y, z, roll, pitch, yaw).
    *   `dimensions`: (length, width, height).
    *   `is_dynamic`: Boolean indicating if the obstacle can move.
*   **Relationships**: Simulated Environment (contained in), Simulated Robot (avoids)
