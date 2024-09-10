# Example of Callbacks

def fetch_data(callback):
    data = {"name": "Alice", "age": 25}
    callback(data)


def handle_data(data):
    print(f"Data received: {data}")


fetch_data(handle_data)  # Handle data after fetching it
