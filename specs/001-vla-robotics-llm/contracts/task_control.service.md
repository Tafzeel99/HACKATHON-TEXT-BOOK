# ROS 2 Service: TaskControl

## Description
ROS 2 Service for sending control commands to manage an ongoing or queued robot task. This allows external systems or user interfaces to interrupt, pause, resume, or modify robot behavior.

## Service Definition

### Request
*   `task_id`: `string` - The unique identifier of the task to be controlled.
*   `command`: `string` - The control command to execute (e.g., "INTERRUPT", "PAUSE", "RESUME", "MODIFY", "ABORT").
*   `new_parameters`: `string` - (Optional) A JSON string containing new parameters or modifications if the command is "MODIFY".

### Response
*   `success`: `bool` - True if the control command was successfully processed and initiated, False otherwise.
*   `status_message`: `string` - A message indicating the outcome of the control command (e.g., "Task paused successfully", "Invalid task ID", "Command not supported").
