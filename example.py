from ct_tcpchat import TcpChat
import logging
import time

# Create a callback function when a message is received
def callback_function(message):
    print(f"\nReceived message: {message}")

# Enter the IP Address from the other computer
connect_to_ip = "192.168.1.50"

# Choose a port for the connection. (Optional. Default = 44785)
port = 44785

# Set the LOG level. (Optional. Default = logging.INFO)
log_level = logging.DEBUG

# Initialize the connection
connection = TcpChat(connect_to_ip=connect_to_ip, callback=callback_function, port=port, log_level=log_level)

# Set the retry interval (optional)
connection.retry_connection_interval = 2

# Example of sending a message from the main thread
if __name__ == "__main__":
    try:
        # Start the connection
        connection.start()

        # Wait for the connection to be established
        while not connection.connected_event.is_set():
            time.sleep(1)

        while connection.connected_event.is_set():
            message = input("Message: ")
            if message:
                connection.send_message(message)

    except KeyboardInterrupt:
        print("\nExiting program...")
        connection.close_connections()
