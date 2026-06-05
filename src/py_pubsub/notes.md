# ROS 2 - Python Publisher & Subscriber

## Objective

Learn the fundamentals of ROS 2 communication by creating a publisher node and a subscriber node using Python (`rclpy`).

---

# Project Overview

This project consists of two ROS 2 nodes:

1. **Publisher Node**

   * Publishes a `String` message every 0.5 seconds.
   * Message format:

     ```
     Hello World: N
     ```
   * `N` increases after every publish.

2. **Subscriber Node**

   * Subscribes to the same topic.
   * Receives incoming messages.
   * Prints received messages to the ROS log.

Communication occurs through a ROS 2 topic named:

```
/topic
```

---

# Concepts Learned

## 1. Node

A node is a single ROS 2 process that performs a specific task.

Examples:

* Camera Node
* Navigation Node
* Motor Controller Node
* Publisher Node
* Subscriber Node

In this project:

```
Publisher Node
Subscriber Node
```

are two separate ROS 2 nodes.

---

## 2. Topic

Topics are communication channels used by ROS 2 nodes.

Publisher:

```
Publisher -> /topic
```

Subscriber:

```
Subscriber <- /topic
```

Multiple nodes can publish and subscribe to the same topic.

---

## 3. Message Types

ROS 2 uses predefined message structures.

Used:

```python
from std_msgs.msg import String
```

Message structure:

```python
msg = String()
msg.data = "Hello World"
```

The message data is transmitted through the topic.

---

## 4. Publisher

Created using:

```python
self.publisher_ = self.create_publisher(
    String,
    'topic',
    10
)
```

Purpose:

* Sends messages to a topic.
* Uses the `String` message type.

Publishing:

```python
self.publisher_.publish(msg)
```

---

## 5. Subscriber

Created using:

```python
self.create_subscription(
    String,
    'topic',
    self.listener_callback,
    10
)
```

Purpose:

* Listens for incoming messages.
* Executes a callback whenever a message arrives.

---

## 6. Callback Functions

Callbacks are functions automatically executed by ROS.

Publisher callback:

```python
timer_callback()
```

Subscriber callback:

```python
listener_callback()
```

ROS calls these functions when an event occurs.

---

## 7. Timer

Created using:

```python
self.create_timer(
    0.5,
    self.timer_callback
)
```

Purpose:

* Runs repeatedly every 0.5 seconds.
* Triggers message publishing.

---

## 8. Logging

Used:

```python
self.get_logger().info(...)
```

Purpose:

* Print ROS-aware logs.
* Includes timestamps and node names.

Example:

```text
[INFO] [timestamp] [publisher]
```

---

## 9. ROS Initialization

Before creating nodes:

```python
rclpy.init()
```

Purpose:

* Starts ROS 2 communication.

---

## 10. ROS Spin

Used:

```python
rclpy.spin(node)
```

Purpose:

* Keeps the node running.
* Allows ROS to process callbacks.

Without spin, the program exits immediately.

---

## 11. Node Shutdown

Used:

```python
node.destroy_node()
rclpy.shutdown()
```

Purpose:

* Cleanly terminate the node.
* Stop ROS communication.

---

## 12. Counter Variable

```python
self.i = 0
```

Purpose:

* Tracks the message number.

Example:

```text
Hello World: 0
Hello World: 1
Hello World: 2
```

---

# ROS 2 Package Structure

```text
ros2-ws/
│
├── src/
│   │
│   └── py_pubsub/
│       ├── package.xml
│       ├── setup.py
│       ├── setup.cfg
│       ├── resource/
│       │   └── py_pubsub
│       │
│       └── py_pubsub/
│           ├── __init__.py
│           ├── publisher_node.py
│           └── subscriber_node.py
│
├── build/
├── install/
└── log/
```

---

# Commands Used

Build package:

```bash
colcon build --packages-select py_pubsub --symlink-install
```

Source workspace:

```bash
source install/setup.bash
```

Run publisher:

```bash
ros2 run py_pubsub talker
```

Run subscriber:

```bash
ros2 run py_pubsub listener
```

---

# Useful ROS CLI Commands

List nodes:

```bash
ros2 node list
```

List topics:

```bash
ros2 topic list
```

Inspect topic:

```bash
ros2 topic info /topic
```

Show topic messages:

```bash
ros2 topic echo /topic
```

Show topic type:

```bash
ros2 topic type /topic
```

---

# Common Errors Encountered

### Missing Module

```text
ModuleNotFoundError
```

Cause:

* Incorrect package structure.
* Incorrect entry point configuration.

---

### Missing Attribute

```text
AttributeError
```

Examples:

```python
self.i
```

not initialized.

```python
self.publisher_
```

name mismatch.

---

### Logger Error

Incorrect:

```python
self.get_logger.info(...)
```

Correct:

```python
self.get_logger().info(...)
```

---

### Logger Formatting Error

Incorrect:

```python
self.get_logger().info(
    "I heard: %s",
    msg.data
)
```

Correct:

```python
self.get_logger().info(
    f"I heard: {msg.data}"
)
```

---

# Key Takeaways

* ROS 2 applications are built from nodes.
* Nodes communicate through topics.
* Topics carry messages.
* Publishers send messages.
* Subscribers receive messages.
* Timers create periodic behavior.
* Callbacks execute automatically when events occur.
* `rclpy.spin()` keeps nodes alive.
* ROS CLI tools help inspect and debug communication.

This project forms the foundation for all future ROS 2 development, including robots, drones, autonomous vehicles, simulations, and distributed robotic systems.
