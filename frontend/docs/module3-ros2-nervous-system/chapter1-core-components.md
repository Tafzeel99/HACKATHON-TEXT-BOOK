# ROS2 Nervous System: Core Components

This module provides an introduction to the core components and concepts essential for building a ROS2-based nervous system. We will explore the fundamental building blocks that enable distributed communication and control in robotic applications.

## 1. ROS2 Nodes

In ROS2, a **node** is an executable process that performs computation. Nodes are typically designed to do one thing well, following the Unix philosophy. For instance, one node might control a motor, another might process camera data, and a third might estimate the robot's pose.

### 1.1. Publisher Node

A **publisher node** is responsible for sending data (messages) on a specific **topic**.

-   **Example: `publisher_node.py`**
    This node creates a publisher for the `/topic` topic, sending `std_msgs/String` messages at a regular interval.
    ```python
    import rclpy
    from rclpy.node import Node
    from std_msgs.msg import String

    class MinimalPublisher(Node):
        def __init__(self):
            super().__init__('minimal_publisher')
            self.publisher_ = self.create_publisher(String, 'topic', 10)
            timer_period = 0.5
            self.timer = self.create_timer(timer_period, self.timer_callback)
            self.i = 0

        def timer_callback(self):
            msg = String()
            msg.data = f'Hello World: {self.i}'
            self.publisher_.publish(msg)
            self.get_logger().info(f'Publishing: "{msg.data}"')
            self.i += 1

    def main(args=None):
        rclpy.init(args=args)
        minimal_publisher = MinimalPublisher()
        rclpy.spin(minimal_publisher)
        minimal_publisher.destroy_node()
        rclpy.shutdown()

    if __name__ == '__main__':
        main()
    ```

### 1.2. Subscriber Node

A **subscriber node** is responsible for receiving data (messages) from a specific **topic**.

-   **Example: `subscriber_node.py`**
    This node creates a subscriber that listens to the `/topic` topic and prints the received `std_msgs/String` messages to the console.
    ```python
    import rclpy
    from rclpy.node import Node
    from std_msgs.msg import String

    class MinimalSubscriber(Node):
        def __init__(self):
            super().__init__('minimal_subscriber')
            self.subscription = self.create_subscription(
                String,
                'topic',
                self.listener_callback,
                10)
            self.subscription

        def listener_callback(self, msg):
            self.get_logger().info(f'I heard: "{msg.data}"')

    def main(args=None):
        rclpy.init(args=args)
        minimal_subscriber = MinimalSubscriber()
        rclpy.spin(minimal_subscriber)
        minimal_subscriber.destroy_node()
        rclpy.shutdown()

    if __name__ == '__main__':
        main()
    ```

## 2. ROS2 Topics

**Topics** are named buses over which nodes exchange messages. They provide an anonymous publish/subscribe communication model, meaning nodes don't need to know about each other to communicate, only about the topics they publish to or subscribe from.

-   **Message Types**: Every topic has a message type (e.g., `std_msgs/String`, `geometry_msgs/Twist`) that defines the structure of the data being sent.
-   **QoS Settings**: Quality of Service (QoS) profiles allow configuration of communication behavior, such as reliability, durability, and history.

## 3. ROS2 Services

**Services** are a request/reply communication mechanism in ROS2. They are used for synchronous interactions where a node sends a request and waits for a response.

-   **Service Server**: Implements the service and provides the response.
-   **Service Client**: Makes requests to the service server.

<h2> 4. ROS2 Actions</h2>

**Actions** are a long-running, asynchronous communication mechanism. They are used for tasks that take a significant amount of time to complete and provide periodic feedback.

-   **Action Server**: Provides the action, offering feedback and a final result.
-   **Action Client**: Sends goals to the action server, receives feedback, and eventually a result.

## 5. ROS2 Parameters

**Parameters** are dynamic values that nodes can expose. They allow configuration of a node's behavior at runtime without recompiling the code.

## 6. ROS2 Launch Files

**Launch files** are XML or Python scripts used to start and configure multiple ROS2 nodes simultaneously. They are crucial for orchestrating complex robotic systems.

import ChapterFooter from '@site/src/components/ChapterFooter';

<ChapterFooter />
