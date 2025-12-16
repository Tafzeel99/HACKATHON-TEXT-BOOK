# ROS 2 Action: CognitivePlanning

## Description
ROS 2 Action for translating a transcribed natural language command into a high-level cognitive plan, using a Large Language Model (LLM). This plan consists of a sequence of abstract steps that can then be translated into executable ROS 2 actions.

## Action Definition

### Goal
*   `transcribed_text`: `string` - The natural language command to be planned.
*   `context_data`: `string` - (Optional) Additional context about the robot's current state or environment (e.g., JSON string).

### Result
*   `cognitive_plan`: `string` - A JSON string representing the high-level plan, including abstract steps and associated parameters.
    *   Example: `{"goal": "Clean the room", "steps": [{"action": "navigate", "target": "kitchen"}, {"action": "pick_up", "object": "cup", "location": "table"}]}`
*   `success`: `bool` - True if planning was successful, False otherwise.
*   `error_message`: `string` - (If not successful) Description of the planning failure.

### Feedback
*   `planning_stage`: `string` - Current stage of the planning process (e.g., "understanding command", "generating steps", "validating plan").
*   `estimated_time_remaining`: `duration` - (Optional) Estimated time until plan completion.
