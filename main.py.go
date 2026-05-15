import requests
from bs4 import BeautifulSoup
import pandas as pd

KEYWORDS = [
    "grant",
    "funding",
    "innovation",
    "Africa",
    "startup"
]

URLS = [
    "https://vc4a.com",
    "https://solve.mit.edu"
]

results = []

headers = {
    "User-Agent": "Mozilla/5.0"
}

for url in URLS:

    try:
        response = requests.get(url, headers=headers)

        soup = BeautifulSoup(response.text, "html.parser")

        text = soup.get_text().lower()

        found = []

        for keyword in KEYWORDS:
            if keyword.lower() in text:
                found.append(keyword)

        if found:

            results.append({
                "website": url,
                "keywords": ", ".join(found)
            })

            print(f"[+] Match found: {url}")

    except Exception as e:
        print("Error:", e)

df = pd.DataFrame(results)

df.to_csv("grants.csv", index=False)

print("\nSaved to grants.csv")