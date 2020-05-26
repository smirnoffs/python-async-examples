import bs4
import requests


def get_html(url: str) -> str:
    resp = requests.get(url)
    return resp.content


def get_title(html: str) -> str:
    soup = bs4.BeautifulSoup(html, "html.parser")
    return soup.title.string


def get_resources():
    sites = (
        "https://google.com",
        "https://amboss.com",
        "https://next.amboss.com/de",
        "https://next.amboss.com/us",
    )
    for url in sites:
        html = get_html(url)
        print(f"{url}: {get_title(html)}")


def main():
    get_resources()
    print("Done.")


if __name__ == "__main__":
    main()
