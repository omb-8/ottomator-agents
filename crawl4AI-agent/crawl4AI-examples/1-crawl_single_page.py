import asyncio
from crawl4ai import *

async def main():
    async with AsyncWebCrawler() as crawler:
        result = await crawler.arun(
            url="https://confluence.uwf.edu/display/public/UWF+Public+Knowledge+Base",
        )
        print(result.markdown)

if __name__ == "__main__":
    asyncio.run(main())