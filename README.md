# TcpChat
TcpChat is a simple Python module for creating a TCP chat connection between two computers to send commands or information.
[GitHub](https://github.com/clevrthings/tcpChat), [PyPi](https://pypi.org/project/ct-tcpchat/)

## Installation
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install TcpChat.

```bash
pip install ct-tcpchat
```

## Simple usage
```python
from ct_tcpchat import TcpChat
import logging

def callback_function(message):
    print(f"Received message: {message}")

connect_to_ip = "192.168.1.50" # Enter the IP Address from the other computer
on_port = 44785 # Choose a port for the connection. (Optional. Default = 44785)

connection = TcpChat(connect_to_ip, callback_function, on_port, log_level=logging.INFO)
connection.start()

# Example of sending a message from the main thread
connection.send_message("Hello from server")
```

## Overview
This library provides two classes for TCP communication: `TcpChat` and `TcpChatBlocking`. Each class serves different purposes based on the need for non-blocking or blocking operations.

### TcpChat (Non-blocking using threading)
The `TcpChat` class is designed for non-blocking TCP communication by leveraging Python's threading capabilities. This class allows for concurrent handling of server and client connections, ensuring that the main application remains responsive and can handle other tasks simultaneously.

**Key Features:**
- **Threading for Concurrency:** The server and client operations run on separate threads, preventing the main application loop from being blocked.
- **Automatic Connection Management:** Automatically handles retries for client connections and accepts incoming connections on the server.
- **Callback Mechanism:** Processes incoming messages using a user-defined callback function.
- **Logging Support:** Includes logging to monitor connection status, message transfers, and errors.

**Usage Example:**
```python
from ct_tcpchat import TcpChat
import logging
import time

def callback_function(message):
    print(f"Received message: {message}")

connect_to_ip = "192.168.1.50"
port = 44785
log_level = logging.DEBUG

connection = TcpChat(connect_to_ip=connect_to_ip, callback=callback_function, port=port, log_level=log_level)
connection.retry_connection_interval = 2

if __name__ == "__main__":
    try:
        connection.start()
        while not connection.connected_event.is_set():
            time.sleep(1)
        while connection.connected_event.is_set():
            message = input("Message: ")
            if message:
                connection.send_message(message)
    except KeyboardInterrupt:
        print("\nExiting program...")
        connection.close_connections()
```

### TcpChatBlocking (Blocking without threading)
The `TcpChatBlocking` class is designed for blocking TCP communication without using threading. This class is suitable for applications where the user wants to control the main loop and manage threading themselves or where the simplicity of blocking operations is desired.

**Key Features:**
- **No Threaded Operation:** Does not use threads, meaning that server and client operations will block the main loop until they complete.
- **User-managed Loop:** Provides a process_events method that the user can call within their main loop to handle incoming connections and messages.
- **Callback Mechanism:** Processes incoming messages using a user-defined callback function.
- **Logging Support:** Includes logging to monitor connection status, message transfers, and errors.

**Usage Example:**
```python
from ct_tcpchat import TcpChatBlocking
import logging
import time

def callback_function(message):
    print(f"Received message: {message}")

connect_to_ip = "192.168.1.50"
port = 44785
log_level = logging.DEBUG

connection = TcpChatBlocking(connect_to_ip=connect_to_ip, callback=callback_function, port=port, log_level=log_level)
connection.retry_connection_interval = 2

if __name__ == "__main__":
    try:
        connection.start()
        while True:
            message = input("Message: ")
            if message:
                connection.send_message(message)
            connection.process_events()
    except KeyboardInterrupt:
        print("\nExiting program...")
        connection.close_connections()
```

#### Key Differences:
1. **Threading:**
   - `TcpChat` uses threading, making it non-blocking and suitable for applications requiring concurrency.
   - `TcpChatBlocking` does not use threading, making it blocking and simpler but requiring the user to manage the main loop.
   
2. **Main Loop Management:**
   - `TcpChat` automatically manages its own threads for server and client operations.
   - `TcpChatBlocking` provides methods to be called in the user's main loop, giving the user more control over the execution flow.

3. **Use Case Suitability:**
   - `TcpChat` is ideal for applications needing responsiveness and concurrency, such as GUIs or real-time systems.
   - `TcpChatBlocking` is ideal for simpler applications or where the user prefers to manage threading themselves, such as in command-line tools or basic scripts.

### Extra functions
```python
TcpChat.get_local_ip() # Returns own IP Address

TcpChat.close_connections() # Closes all the connections

TcpChat.retry_connection_interval = 2 # Set the retry interval (Default = 5 seconds)
```

##### License
MIT