import validators
import requests

URLS = ["https://empty-smoke.surge.sh/login",
        "https://achang-jobly.onrender.com",
        "https://achang-warbler.onrender.com"]


def ping_urls(urls):
    """Pings each URL listed"""
    for url in urls:
        if not validators.url(url):
            print(f"not valid url: {url}")
        else:
            requests.get(url)
            print(f"successfully pinged: {url}")


def run():
    ping_urls(URLS)


if __name__ == "__main__":
    run()
