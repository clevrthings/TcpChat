from ct_tcpchat import TcpChatBlocking
import logging

# Create a callback function when a message is received
def callback_function(message):
    print(f"Received message: {message}")

# Enter the IP Address from the other computer
connect_to_ip = "192.168.1.50"

# Choose a port for the connection. (Optional. Default = 44785)
port = 44785

# Set the LOG level. (Optional. Default = logging.INFO)
log_level = logging.DEBUG

# Initialize the connection
connection = TcpChatBlocking(connect_to_ip=connect_to_ip, callback=callback_function, port=port, log_level=log_level)

# Set the retry interval (optional)
connection.retry_connection_interval = 5

if __name__ == "__main__":
    try:
        # Start the connection
        connection.start()

        # Main loop to handle events and user input
        while True:
            message = input("Message: ")
            if message:
                connection.send_message(message)
            connection.process_events()

    except KeyboardInterrupt:
        print("\nExiting program...")
        connection.close_connections()
