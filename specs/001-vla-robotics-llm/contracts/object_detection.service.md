# ROS 2 Service: ObjectDetection

## Description
ROS 2 Service for requesting real-time object identification and localization using the robot's computer vision system.

## Service Definition

### Request
*   `camera_feed`: `sensor_msgs/msg/Image` - The current camera image or video stream frame to analyze.
*   `object_type_hint`: `string` - (Optional) A hint for the type of object to search for (e.g., "cup", "book"). Can assist in targeted detection.

### Response
*   `detected_objects`: `visualization_msgs/msg/MarkerArray` or similar - A list of detected objects. Each object includes:
    *   `object_id`: `string` - Unique identifier for the detected object.
    *   `object_type`: `string` - Classification of the object (e.g., "cup", "book").
    *   `pose`: `geometry_msgs/msg/PoseStamped` - 3D pose (position and orientation) of the object relative to a known frame.
    *   `confidence`: `float` - Confidence score for the detection (0.0 to 1.0).
*   `success`: `bool` - True if the detection service processed the request, False if there was an internal error.
*   `error_message`: `string` - (If not successful) Description of the error.
