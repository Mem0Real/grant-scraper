import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

visited = set()

def crawl(url, depth=1):

    if depth == 0:
        return []

    if url in visited:
        return []

    visited.add(url)

    print(f"[+] Crawling: {url}")

    links_found = []

    try:

        headers = {
            "User-Agent": "Mozilla/5.0"
        }

        response = requests.get(
            url,
            headers=headers,
            timeout=10
        )

        soup = BeautifulSoup(response.text, "html.parser")

        for link in soup.find_all("a", href=True):

            full_url = urljoin(url, link["href"])

            if full_url.startswith("http"):

                links_found.append(full_url)

    except Exception as e:
        print("Error:", e)

    return links_found