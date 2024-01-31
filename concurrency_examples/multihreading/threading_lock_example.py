import threading
import time

# Shared counter variable
counter = 0

# Number of threads to create
num_threads = 5

# Lock to synchronize access to the shared counter
counter_lock = threading.Lock()

def increment_counter():
    global counter
    for _ in range(100000):
        # Acquire the lock before updating the shared counter
        with counter_lock:
            counter += 1
        # Release the lock to allow other threads to acquire it

def main():
    # Create a list to hold thread objects
    threads = []

    # Create and start threads
    for _ in range(num_threads):
        thread = threading.Thread(target=increment_counter)
        thread.start()
        threads.append(thread)

    # Wait for all threads to complete
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    start_time = time.time()
    main()
    end_time = time.time()

    # Print the final counter value and execution time
    print(f"Final Counter Value: {counter}")
    print(f"Total execution time: {end_time - start_time} seconds")
