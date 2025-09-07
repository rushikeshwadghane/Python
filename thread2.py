import threading

# Shared variable
counter = 0
lock = threading.Lock()

# Function to increment the counter with a lock
def increment():
    global counter
    for _ in range(100000):
        with lock:
            counter += 1

# Create threads
thread1 = threading.Thread(target=increment)
thread2 = threading.Thread(target=increment)

# Start threads
thread1.start()
thread2.start()

# Wait for both threads to finish
thread1.join()
thread2.join()

# Print the final value of counter
print(f"Counter: {counter}")
