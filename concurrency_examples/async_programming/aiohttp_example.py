import aiohttp
import asyncio
import time


async def fetch_url(session, url):
    """Fetch a URL asynchronously using aiohttp."""
    async with session.get(url) as response:
        return await response.text()


async def main():
    # List of URLs to fetch concurrently
    urls_to_fetch = [
        "https://www.example.com",
        "https://www.example.org",
        "https://www.example.net",
        # Add more URLs as needed
    ]

    # Create an aiohttp ClientSession
    async with aiohttp.ClientSession() as session:
        # Create tasks for fetching each URL concurrently
        tasks = [fetch_url(session, url) for url in urls_to_fetch]

        # Gather and await the results of all tasks
        results = await asyncio.gather(*tasks)

        # Process the results (in this example, simply printing them)
        for url, result in zip(urls_to_fetch, results):
            print(f"Content of {url}: {result[:100]}...")


if __name__ == "__main__":
    start_time = time.time()

    # Run the asynchronous event loop
    asyncio.run(main())

    end_time = time.time()
    print(f"Total execution time: {end_time - start_time} seconds")
