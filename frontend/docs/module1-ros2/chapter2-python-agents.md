---
sidebar_position: 2
---

# Chapter 2: Python Agents with ROS 2

This chapter explains how to use Python to create ROS 2 nodes and communicate with other nodes in the ROS 2 ecosystem. Python is a popular language for robotics due to its ease of use and the large number of available libraries for AI and machine learning. In this chapter, you will learn how to use the `rclpy` library to write ROS 2 nodes in Python.

## The `rclpy` Library

`rclpy` is the official Python client library for ROS 2. It provides a Pythonic interface to all of ROS 2's core features, including nodes, topics, services, and parameters. With `rclpy`, you can write ROS 2 nodes in Python with the same level of functionality as C++ nodes.

### Publisher/Subscriber Example

Here is a conceptual example of a simple publisher and subscriber using `rclpy`.

**Publisher:**
```python
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class MyPublisher(Node):
    def __init__(self):
        super().__init__('my_publisher')
        self.publisher_ = self.create_publisher(String, 'my_topic', 10)
        self.timer = self.create_timer(0.5, self.timer_callback)

    def timer_callback(self):
        msg = String()
        msg.data = 'Hello, ROS 2!'
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%s"' % msg.data)

def main(args=None):
    rclpy.init(args=args)
    my_publisher = MyPublisher()
    rclpy.spin(my_publisher)
    my_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
```

**Subscriber:**
```python
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class MySubscriber(Node):
    def __init__(self):
        super().__init__('my_subscriber')
        self.subscription = self.create_subscription(
            String,
            'my_topic',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning

    def listener_callback(self, msg):
        self.get_logger().info('I heard: "%s"' % msg.data)

if __name__ == '__main__':
    main()
```

## Python ROS 2 Node Lifecycle and Interaction

This sequence diagram details the typical lifecycle of a Python ROS 2 node, from initialization to shutdown, highlighting its interaction with the `rclpy` library and other ROS 2 components.

```mermaid
sequenceDiagram
    participant P as Python Script
    participant R as rclpy Library
    participant N as ROS2 Node
    participant T as ROS2 Topic
    participant O as Other ROS2 Node

    P->>R: Import rclpy
    P->>R: Initialize (rclpy.init())
    P->>N: Create Node (Node("my_node"))
    N->>R: Use rclpy functions
    N-->>T: Publish Message
    T-->>N: Subscribe to Message
    N<->>O: Communicate (via Topics/Services)
    P->>R: Spin Node (rclpy.spin())
    P->>R: Shutdown (rclpy.shutdown())
```

## Integrating AI Agents

The publisher/subscriber model is a powerful way to integrate AI agents into a ROS 2 system. For example, you could have an AI agent that processes camera images to detect objects. This agent could be a ROS 2 node that subscribes to an `/image` topic, performs the object detection, and then publishes the results to an `/object_detections` topic.

Other nodes in the system could then subscribe to the `/object_detections` topic to use the information for tasks such as navigation or manipulation. This modular approach allows you to develop and test your AI agent independently of the rest of the robotics system.
