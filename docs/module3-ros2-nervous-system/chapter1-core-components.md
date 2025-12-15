# ROS2 Nervous System: Core Components

This module provides an introduction to the core components of the ROS2 Nervous System.

## Publisher Node

The publisher node (`publisher_node.py`) is responsible for sending messages on a specific ROS2 topic. It periodically publishes "Hello World" strings to the `/topic` topic.

## Subscriber Node

The subscriber node (`subscriber_node.py`) is responsible for receiving messages from a specific ROS2 topic. It listens to the `/topic` topic and logs the received "Hello World" strings.