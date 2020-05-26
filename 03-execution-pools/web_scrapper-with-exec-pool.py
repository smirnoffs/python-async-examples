from concurrent.futures import Future
from concurrent.futures.thread import ThreadPoolExecutor

import bs4
import requests


def main():
    urls = [
        "https://google.com",
        "https://amboss.com",
        "https://next.amboss.com/de",
        "https://next.amboss.com/us",
    ]

    work = []

    with ThreadPoolExecutor(max_workers=4) as executor:
        for url in urls:
            f: Future = executor.submit(get_title, url)
            work.append(f)

    for f in work:
        print("{}".format(f.result()))
    print("Done.")


def get_title(url: str) -> str:
    resp = requests.get(url)
    resp.raise_for_status()

    html = resp.text

    soup = bs4.BeautifulSoup(html, "html.parser")
    return soup.title.string


if __name__ == "__main__":
    main()
