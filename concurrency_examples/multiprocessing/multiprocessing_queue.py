import multiprocessing
import time

def producer(queue, data):
    """A producer function that puts data into the queue."""
    for item in data:
        time.sleep(0.5)  # Simulate some processing time
        queue.put(item)
        print(f"Produced: {item}")

def consumer(queue):
    """A consumer function that gets and processes data from the queue."""
    while True:
        item = queue.get()
        if item is None:
            break  # Exit the loop when the sentinel value is received
        # Simulate processing of the item
        time.sleep(1)
        print(f"Consumed: {item}")

def main():
    # Shared queue for inter-process communication
    shared_queue = multiprocessing.Queue()

    # Data to be produced and consumed
    data_to_produce = [1, 2, 3, 4, 5]
    sentinel = None  # A sentinel value to signal the end of data

    # Creating and starting the producer and consumer processes
    producer_process = multiprocessing.Process(target=producer, args=(shared_queue, data_to_produce))
    consumer_process = multiprocessing.Process(target=consumer, args=(shared_queue,))

    producer_process.start()
    consumer_process.start()

    # Waiting for the producer to finish producing
    producer_process.join()

    # Adding sentinel value to signal the end of data
    shared_queue.put(sentinel)

    # Waiting for the consumer to finish consuming
    consumer_process.join()

if __name__ == "__main__":
    start_time = time.time()
    main()
    end_time = time.time()
    print(f"Total execution time: {end_time - start_time} seconds")
