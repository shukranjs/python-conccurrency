import multiprocessing
import time

def square_worker(number):
    """A worker function to calculate the square of a number."""
    result = number * number
    process_id = multiprocessing.current_process().name
    print(f"Process {process_id}: Square of {number} is {result}")
    return result

def main():
    # List of numbers to square
    numbers_to_square = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # Number of worker processes to create
    num_processes = 4

    # Using a multiprocessing pool to parallelize the computation
    with multiprocessing.Pool(num_processes) as pool:
        # Mapping the square_worker function to the list of numbers
        results = pool.map(square_worker, numbers_to_square)

    # Print the results
    print(f"Results: {results}")

if __name__ == "__main__":
    start_time = time.time()
    main()
    end_time = time.time()
    print(f"Total execution time: {end_time - start_time} seconds")
