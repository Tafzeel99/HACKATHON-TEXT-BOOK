# ROS 2 Action: CommandTranscription

## Description
ROS 2 Action for transcribing natural language voice commands received from the user into text. This action encapsulates the interaction with an Automatic Speech Recognition (ASR) system, such as OpenAI Whisper.

## Action Definition

### Goal
*   `audio_data`: `sensor_msgs/msg/CompressedImage` or similar (representing raw audio stream or file) - The audio input to be transcribed.

### Result
*   `transcribed_text`: `string` - The text content of the transcribed command.
*   `confidence`: `float` - A confidence score (0.0 to 1.0) for the transcription.

### Feedback
*   `status_message`: `string` - Current status of the transcription process (e.g., "processing audio", "transcribing", "awaiting input").
*   `progress_percentage`: `float` - (Optional) Percentage of audio processed.
