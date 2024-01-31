import concurrent.futures
import requests
import time


def download_page(url):
    """Download a web page and print its length."""
    response = requests.get(url)
    print(f"Downloaded {url}: {len(response.text)} characters")


def main():
    # List of URLs to download concurrently
    urls = [
        "https://www.example.com",
        "https://www.example.org",
        "https://www.example.net",
    ]

    # Set the maximum number of threads in the thread pool
    max_threads = 3

    # Using ThreadPoolExecutor to download pages concurrently
    with concurrent.futures.ThreadPoolExecutor(max_threads) as executor:
        # Submit download_page function for each URL in the list
        # The results() method waits for all tasks to complete and collects their results
        futures = [executor.submit(download_page, url) for url in urls]
        concurrent.futures.wait(futures)


if __name__ == "__main__":
    start_time = time.time()
    main()
    end_time = time.time()
    print(f"Total execution time: {end_time - start_time} seconds")
