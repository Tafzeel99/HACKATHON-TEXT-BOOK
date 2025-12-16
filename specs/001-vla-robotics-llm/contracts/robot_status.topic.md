# ROS 2 Topic: RobotStatus

## Description
ROS 2 Topic for continuously broadcasting the current operational status, task progress, and health information of the simulated robot to interested subscribers (e.g., user interface, monitoring systems).

## Message Type (conceptual)

`vla_interfaces/msg/RobotStatus` (Custom Message Type)

### Fields
*   `header`: `std_msgs/msg/Header` - Standard ROS 2 message header, including timestamp and frame ID.
*   `robot_id`: `string` - Unique identifier for the robot.
*   `current_task`: `string` - Description of the high-level task the robot is currently performing (e.g., "Cleaning the room", "Idle", "Charging").
*   `task_progress`: `float` - Progress of the current task (0.0 to 1.0), or -1 if no task is active or progress is not applicable.
*   `robot_state`: `string` - Detailed operational state (e.g., "NAVIGATING", "MANIPULATING", "PERCEIVING", "ERROR", "PAUSED", "IDLE").
*   `battery_level`: `float` - Current battery charge level (0.0 to 1.0).
*   `error_message`: `string` - (Optional) Description of any active error or warning conditions.
*   `current_pose`: `geometry_msgs/msg/PoseStamped` - Current pose of the robot.
