# Import the ROS 2 Python library
import rclpy

# Import the Node base class used to create ROS 2 nodes
from rclpy.node import Node

# Import the String message type
from std_msgs.msg import String

# Publisher node that sends messages to a topic
class Publisher(Node):

	def __init__(self):
		# Initialize this node with the name "publisher"
		super().__init__('publisher')

		# Create a publisher that sends String messages on the "topic" topic
		# The queue size of 10 means ROS can store up to 10 messages if needed
		self.publisher_ = self.create_publisher(
			String,
			'topic',
			10)

		# Publish a message every 0.5 seconds
		timer_period = 0.5 
		self.timer = self.create_timer(timer_period, self.timer_callback)
		self.i = 0

	def timer_callback(self):
		# Create a new String message
		msg = String()

		# Store the message text inside the message object
		msg.data = 'Hello World: %d' % self.i 

		# Publish the message on the topic
		self.publisher_.publish(msg)

		# Print the published message to the ROS log
		self.get_logger().info('Publishing: "%s"' % msg.data) 

		# Increase the counter for the next message
		self.i +=1

def main (args=None):
	# Start the ROS 2 communication system
	rclpy.init(args=args)

	# Create an instance of the publisher node
	publisher = Publisher()

	# Keep the node running and process timer events
	rclpy.spin(publisher)

	# Destroy the node explicitly
	# (optional - otherwise it will be done automatically
	# when the garbage collector destroys the node object)
	publisher.destroy_node()

	# Shut down ROS 2
	rclpy.shutdown()

# Run main() only when this file is executed directly
if __name__ == '__main__':
	main()

