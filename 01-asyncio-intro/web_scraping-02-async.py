import asyncio

import aiohttp
import bs4

global loop


async def get_html(url: str) -> str:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            resp.raise_for_status()

            return await resp.text()


def get_title(html: str) -> str:
    soup = bs4.BeautifulSoup(html, "html.parser")
    return soup.title.string


async def get_resources():
    sites = (
        "https://google.com",
        "https://amboss.com",
        "https://next.amboss.com/de",
        "https://next.amboss.com/us",
    )
    tasks = []
    for url in sites:
        tasks.append((url, loop.create_task(get_html(url))))
    for url, t in tasks:
        html = await t
        print(f"{url}: {get_title(html)}")


def main():
    global loop
    loop = asyncio.get_event_loop()
    loop.run_until_complete(get_resources())
    print("Done.")


if __name__ == "__main__":
    main()
