# ROS 2 Action: ExecuteRobotActions

## Description
ROS 2 Action for executing a sequence of ROS 2 primitive actions derived from a cognitive plan. This action orchestrates lower-level robot behaviors like navigation, manipulation, and perception.

## Action Definition

### Goal
*   `ros_action_sequence`: `string` - A JSON string representing the ordered sequence of ROS 2 primitive actions to execute.
    *   Example: `[{"type": "navigate_to_pose", "x": 1.0, "y": 0.5, "yaw": 0.0}, {"type": "manipulate_object", "object_id": "cup", "action": "grasp"}]`
*   `interrupt_policy`: `string` - (e.g., "abort_on_interrupt", "pause_on_interrupt", "complete_current_then_interrupt") - Defines how to handle external interruptions.

### Result
*   `task_completed`: `bool` - True if the entire sequence was completed successfully, False otherwise.
*   `final_status`: `string` - A detailed status message upon completion or failure.
*   `executed_actions`: `string` - (Optional) A JSON string detailing which actions were executed.

### Feedback
*   `current_action`: `string` - Description of the action currently being executed (e.g., "navigating to target", "grasping object").
*   `action_progress`: `float` - Progress of the current action (0.0 to 1.0).
*   `robot_status`: `string` - Overall status of the robot (e.g., "moving", "idle", "error").
*   `estimated_time_to_completion`: `duration` - Estimated time for the entire sequence to complete.
