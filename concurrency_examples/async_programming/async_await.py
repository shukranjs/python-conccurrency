import asyncio
import time


async def fetch_url(url):
    """Fetch a URL asynchronously using asyncio."""
    print(f"Start fetching: {url}")
    # Simulate some async I/O work (e.g., fetching data from a server)
    await asyncio.sleep(1)
    print(f"Finished fetching: {url}")
    return f"Data from {url}"


async def main():
    # List of URLs to fetch concurrently
    urls_to_fetch = [
        "https://www.example.com",
        "https://www.example.org",
        "https://www.example.net",
        # Add more URLs as needed
    ]

    # Create tasks for fetching each URL concurrently
    tasks = [fetch_url(url) for url in urls_to_fetch]

    # Use asyncio.gather to await the results of all tasks concurrently
    results = await asyncio.gather(*tasks)

    # Process the results (in this example, simply printing them)
    for url, result in zip(urls_to_fetch, results):
        print(f"Result from {url}: {result}")


if __name__ == "__main__":
    start_time = time.time()

    # Run the asynchronous event loop
    asyncio.run(main())

    end_time = time.time()
    print(f"Total execution time: {end_time - start_time} seconds")
